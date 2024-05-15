from pymongo import MongoClient
from constants import MONGODB_STR, MONGODB_DB

# Connect to MongoDB
def connect_to_db():
    client = MongoClient(MONGODB_STR)
    return client[MONGODB_DB]

if __name__ == '__main__':
    db = connect_to_db()
    print("mongodb database connected")
