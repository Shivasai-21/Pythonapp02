from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client.chatdb

def save_message(room, user, msg):
    db.messages.insert_one({"room": room, "user": user, "msg": msg})

def get_messages(room, limit=50):
    return list(db.messages.find({"room": room}).sort("_id", -1).limit(limit))
