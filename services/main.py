from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Establish connection to MongoDB
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Accounts']
credentials = db['Credentials']

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This is for development only; specify your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    password: str

@app.post("/signup/")
async def signup(user: User):
    user_id = add_user(user.email, user.password, user.email)  # Assuming username and email are the same
    return {"user_id": str(user_id), "message": "User created successfully"}

from werkzeug.security import generate_password_hash

def add_user(username, password, email):
    hashed_password = generate_password_hash(password)
    user_data = {"username": username, "email": email, "password": hashed_password}
    result = credentials.insert_one(user_data)
    return result.inserted_id
