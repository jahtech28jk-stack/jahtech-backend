from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["jahtech_db"]
users_collection = db["users"]

@app.get("/")
def home():
    return {"message": "JAHATECH IS LIVE 🔥"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))
    return {"users": users}

@app.post("/users")
def create_user(name: str, email: str):
    user = {"name": name, "email": email}
    users_collection.insert_one(user)
    return {"message": "User created", "user": user}
