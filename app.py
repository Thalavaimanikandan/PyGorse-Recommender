from flask import Flask, request, jsonify
from pymongo import MongoClient
from gorse import Gorse  # ✅ Use the Gorse SDK

app = Flask(__name__)

# === GORSE CONFIG ===
GORSE_ENDPOINT = "http://127.0.0.1:8088"
GORSE_API_KEY = "zhenghaoz"

# Create a Gorse client
gorse_client = Gorse(GORSE_ENDPOINT, GORSE_API_KEY)

# === MONGODB CONFIG ===
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["insta_clone"]
users_collection = db["users"]
posts_collection = db["posts"]
likes_collection = db["likes"]

# === HOME ===
@app.route("/")
def home():
    return jsonify({"message": "MongoDB + Gorse + Flask connected (SDK version)!"})


# === ADD USER FEEDBACK (like) ===
@app.route("/feedback", methods=["POST"])
def add_feedback():
    data = request.json
    user_id = data.get("user_id")
    item_id = data.get("item_id")

    # 1️⃣ Store feedback in MongoDB
    likes_collection.insert_one({"user_id": user_id, "item_id": item_id})

    # 2️⃣ Send feedback to Gorse via SDK
    feedback = [{
        "FeedbackType": "like",
        "UserId": user_id,
        "ItemId": item_id
    }]

    result = gorse_client.insert_feedbacks(feedback)
    return jsonify({"status": "ok", "gorse_response": result})


# === SYNC USERS FROM MONGODB TO GORSE ===
@app.route("/sync/users", methods=["POST"])
def sync_users():
    users = [{"UserId": str(u["_id"])} for u in users_collection.find()]
    result = gorse_client.insert_users(users)
    return jsonify({"synced_users": len(users), "gorse_response": result})


# === SYNC POSTS (ITEMS) TO GORSE ===
@app.route("/sync/items", methods=["POST"])
def sync_items():
    items = []
    for post in posts_collection.find():
        items.append({
            "ItemId": str(post["_id"]),
            "Categories": post.get("tags", []),
            "Labels": [post.get("caption", "")],
            "Comment": post.get("description", "")
        })
    result = gorse_client.insert_items(items)
    return jsonify({"synced_items": len(items), "gorse_response": result})


# === GET RECOMMENDATIONS FOR USER ===
@app.route("/recommend/<user_id>", methods=["GET"])
def recommend(user_id):
    recommendations = gorse_client.get_recommend(user_id, n=5)
    recommended_ids = [r["Id"] for r in recommendations] if recommendations else []

    # Fetch actual post details from MongoDB
    post_details = list(posts_collection.find({"_id": {"$in": recommended_ids}}))
    for post in post_details:
        post["_id"] = str(post["_id"])

    return jsonify({
        "recommended_ids": recommended_ids,
        "recommended_items": post_details
    })


if __name__ == "__main__":
    app.run(debug=True)
