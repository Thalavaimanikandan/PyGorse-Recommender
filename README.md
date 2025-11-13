## 📘 README.md

```markdown
# 🧠 PyGorse Recommendation System

A Flask-based API that integrates with **Gorse** (an open-source recommender system) and **MongoDB** to provide personalized recommendations — similar to Instagram’s post suggestion logic.

---

## 🚀 Features

- 🔗 Connects **Flask** → **Gorse** → **MongoDB**
- 📦 Syncs users and items (posts) from MongoDB to Gorse
- ❤️ Sends user feedback (likes, follows, etc.) to Gorse
- 🎯 Fetches personalized recommendations for users
- 🧩 Easy to extend for real-world apps (e.g., social media, e-commerce)

---

## 🛠️ Tech Stack

| Component | Description |
|------------|--------------|
| **Flask** | REST API backend |
| **MongoDB** | Application database (users, posts, likes) |
| **Gorse** | Recommendation engine |
| **PyMongo** | Python driver for MongoDB |
| **Requests** | HTTP client to communicate with Gorse |

---

## 📂 Project Structure

```

PyGorse-main/
│
├── app.py                # Flask + Gorse + MongoDB integration
├── config.yaml           # (optional) Gorse config
├── requirements.txt      # Python dependencies
├── venv/                 # Python virtual environment
└── README.md             # Documentation (this file)

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/PyGorse-main.git
cd PyGorse-main
````

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask pymongo requests
```

---

### 4️⃣ Run MongoDB

Make sure MongoDB is installed and running:

```bash
sudo systemctl start mongod
```

Check if it’s active:

```bash
mongo
show dbs
```

---

### 5️⃣ Run Gorse

Download and start the Gorse server:

```bash
wget -O gorse_linux_amd64.zip https://github.com/gorse-io/gorse/releases/latest/download/gorse_linux_amd64.zip
tar -xzf gorse_linux_amd64.tar.gz
 chmod +x gorse-in-one
 ./gorse-in-one -c config.
```

By default:

* **Gorse Dashboard** → `http://127.0.0.1:8088/apidocs`
* **API Endpoint** → `http://127.0.0.1:8088/api/`

---

### 6️⃣ Run Flask App

```bash
python app.py
```

Now open in browser:

```
http://127.0.0.1:5000
```

You should see:

```json
{"message": "MongoDB + Gorse + Flask connected!"}
```

---

## 🔗 API Endpoints

### ✅ Home

```bash
GET /
```toml

**Response**

```json
{"message": "MongoDB + Gorse + Flask connected!"}
```

---

### 👥 Sync Users

```bash
POST /sync/users
```

Syncs all MongoDB users to Gorse.

---

### 🖼️ Sync Items (Posts)

```bash
POST /sync/items
```

Syncs all MongoDB posts to Gorse.

---

### ❤️ Add Feedback

```bash
POST /feedback
```

**Request**

```json
{
  "user_id": "user123",
  "item_id": "post456"
}
```

**Response**

```json
{"RowAffected": 1}
```

---

### 🎯 Get Recommendations

```bash
GET /recommend/<user_id>
```

**Example**

```bash
curl http://127.0.0.1:5000/recommend/user123
```

**Response**

```json
{
  "recommended_items": [
    {
      "_id": "post456",
      "caption": "Beach Sunset 🌅",
      "tags": ["travel", "sunset", "nature"],
      "description": "Enjoying sunset by the beach."
    }
  ]
}
```

---

## 🧩 MongoDB Schema (Example)

### Users

```json
{
  "_id": "user123",
  "name": "Alice",
  "email": "alice@example.com"
}
```

### Posts

```json
{
  "_id": "post456",
  "caption": "Beautiful sunset!",
  "tags": ["sunset", "travel"],
  "description": "Enjoying the sunset view."
}
```

### Likes

```json
{
  "user_id": "user123",
  "item_id": "post456"
}
```

---

## 🔁 Typical Workflow

1️⃣ Insert new users/posts into MongoDB
2️⃣ Sync users and posts with Gorse
3️⃣ Send feedback (likes/follows) to Gorse
4️⃣ Request recommendations for users

---

## 🧠 Example Workflow in Terminal

```bash
# Add Feedback
curl -X POST http://127.0.0.1:5000/feedback \
     -H "Content-Type: application/json" \
     -d '{"user_id": "0-vortex", "item_id": "00-evan:shattered-pixel-dungeon"}'

# Sync Users
curl -X POST http://127.0.0.1:5000/sync/users

# Sync Items
curl -X POST http://127.0.0.1:5000/sync/items

# Get Recommendations
curl http://127.0.0.1:5000/recommend/0-vortex
```

---

## 🧰 Troubleshooting

| Issue                                                   | Possible Fix                                                |
| ------------------------------------------------------- | ----------------------------------------------------------- |
| `404: Page Not Found`                                   | Check the API path (`/api/users` not `/api/userss`)         |
| `Connection refused`                                    | Gorse or MongoDB may not be running                         |
| `ImportError: cannot import name 'requests' from flask` | Use `from flask import request` (not requests)              |
| No recommendations                                      | Add more feedback data, then recheck `/recommend/<user_id>` |

---

## 🧑‍💻 Author

**Thalavai Manikandan**
💼 Full Stack Developer | AI Integration Enthusiast
📧 [your-email@example.com](mailto:thalavaimanikandan24@gmail.com)

---

## 🪄 Future Enhancements

* 🧮 Add “view” and “follow” feedback types
* 🤖 Integrate TensorFlow models with Gorse
* 📈 Build a dashboard to visualize recommendation metrics
* 🌍 Deploy with Docker Compose (Flask + Gorse + MongoDB)

---

## 🏁 License

MIT License © 2025 Thalavai Manikandan

```

---

```
