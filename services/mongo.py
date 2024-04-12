"""
This module provides functions to manage user accounts. It allows adding,
deleting, and authenticating users using a MongoDB database.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()

# Establish connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Specify the database and collection
db = client.Accounts
credentials = db.Credentials


@app.post("/process-button-click/")
def process_button_click():
    """does a thing

    Returns:
        _type_: _description_
    """
    # Your backend logic here
    return {"message": "Button was clicked and processed by FastAPI backend!"}


def add_user(username, password, email):
    """
    Adds a new user to the database with hashed password.

    Parameters:
    username (str): Username of the new user.
    password (str): Plain text password to be hashed and stored.
    email (str): Email of the new user.

    Returns:
    ObjectId: MongoDB ID of the inserted user document.
    """
    user_info = {
        "username": username,
        "password": generate_password_hash(password),
        "email": email
    }
    # Inserting the document into the collection
    insert_result = credentials.insert_one(user_info)
    return insert_result.inserted_id

def delete_user(username):
    """
    Deletes a user based on username.

    Parameters:
    username (str): Username of the user to be deleted.

    Returns:
    bool: True if a user was deleted, False otherwise.
    """
    query = {"username": username}
    result = credentials.delete_one(query)
    return result.deleted_count > 0

def authenticate_user(username, password):
    """
    Authenticates a user based on username and password.

    Parameters:
    username (str): The username of the user trying to authenticate.
    password (str): The password provided by the user for authentication.

    Returns:
    bool: True if authentication is successful, False otherwise.
    """
    user = credentials.find_one({"username": username})
    
    if user and check_password_hash(user['password'], password):
        return True  # Authentication successful
    return False  # Authentication failed

