from flask import request, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db

def register_user(username, password):
    hashed = generate_password_hash(password)
    db.users.insert_one({"username": username, "password": hashed})

def login_user(username, password):
    user = db.users.find_one({"username": username})
    if user and check_password_hash(user['password'], password):
        session['user'] = username
        return True
    return False
