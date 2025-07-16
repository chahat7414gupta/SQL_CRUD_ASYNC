# 🗨️ Async Chat API with FastAPI & SQLite

A simple **asynchronous chat backend** built with **FastAPI**, **async SQLAlchemy**, and **SQLite**, supporting full CRUD for `User` and `Message` models.

---

## 🚀 Features

- Async SQLAlchemy 2.0 ORM with `aiosqlite`
- Users and Messages with sender → receiver relationship
- Full CRUD for both models
- Chat conversation history between two users
- SQLite database (no setup required)
- REST API endpoints with FastAPI
- Easy to extend (e.g., WebSockets, FAISS for semantic chat, etc.)

---

## 📁 Project Structure

.
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── schemas.py
│ ├── crud.py
│ └── routers/
│ ├── users.py
│ └── messages.py
├── requirements.txt
└── README.md

yaml


---

## 🛠️ Installation

### 1. Clone and create virtual environment

```bash
git clone https://github.com/chahat7414gupta/SQL_CRUD_ASYNC/
```
```bash
cd chat-app
```
```bash
python3.10 -m venv venv
```
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the app
```bash
uvicorn app.main:app --reload
```
Then open: http://127.0.0.1:8000/docs

💬 API Usage (cURL)
👤 Create a User
```bash

curl -X POST http://127.0.0.1:8000/users/ \
-H "Content-Type: application/json" \
-d '{"name": "Alice", "email": "alice@example.com"}'
```
👤 List Users
```bash

curl http://127.0.0.1:8000/users/
```
💌 Send a Message
```bash
curl -X POST http://127.0.0.1:8000/messages/ \
-H "Content-Type: application/json" \
-d '{"sender_id": 1, "receiver_id": 2, "content": "Hello there!"}'
```
💌 Get All Messages
```bash

curl http://127.0.0.1:8000/messages/
```
🔁 Get Conversation Between Two Users
```bash

curl "http://127.0.0.1:8000/messages/conversation?user1=1&user2=2"
```
🧠 Extensibility Ideas
Add WebSocket support for real-time chat

Use OpenAI or Sentence Transformers to embed messages

Add FAISS vector search to semantically retrieve past messages

Add authentication (JWT) and user sessions

📦 Tech Stack
Python 3.10

FastAPI

SQLAlchemy 2.0 Async

SQLite (aiosqlite)

Uvicorn

👤 Author
Chahat Gupta


