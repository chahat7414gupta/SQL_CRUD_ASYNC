# FastAPI Async SQLAlchemy CRUD (SQLite)

This project demonstrates a simple asynchronous CRUD API using **FastAPI**, **SQLAlchemy (async ORM)**, and **SQLite**. It includes two models:

- `User`
- `Message` (related to `User`)

---

## 🚀 Features

- Async SQLAlchemy ORM with `aiosqlite`
- Full CRUD for `User` and `Message`
- SQLite database (no external DB setup needed)
- Clean separation of concerns: models, schemas, crud, routers
- FastAPI interactive docs at `/docs`
- Graceful error handling (e.g., duplicate email)

---

## 📦 Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

   ```
2. **Run the FastAPI app**

 ```bash
uvicorn app.main:app --reload

```
🧪 Testing via cURL
👤 User Endpoints
✅ Create User

 ```bash
curl -X POST http://127.0.0.1:8000/users/ \
-H "Content-Type: application/json" \
-d '{"name": "Alice", "email": "alice@example.com"}'

```
📥 Get All Users
 ```bash

curl http://127.0.0.1:8000/users/
 ```
📥 Get User by ID
 ```bash

curl http://127.0.0.1:8000/users/1
 ```
🔁 Update User
 ```bash

curl -X PUT http://127.0.0.1:8000/users/1 \
-H "Content-Type: application/json" \
-d '{"name": "Alice Updated", "email": "alice_new@example.com"}'
 ```

❌ Delete User
 ```bash

curl -X DELETE http://127.0.0.1:8000/users/1
 ```
💬 Message Endpoints
Make sure the user ID exists (e.g., user_id = 1)

✅ Create Message
 ```bash

curl -X POST http://127.0.0.1:8000/messages/ \
-H "Content-Type: application/json" \
-d '{"content": "Hello World", "user_id": 1}'
 ```
📥 Get All Messages
 ```bash

curl http://127.0.0.1:8000/messages/
 ```
📥 Get Message by ID
 ```bash

curl http://127.0.0.1:8000/messages/1
 ```
