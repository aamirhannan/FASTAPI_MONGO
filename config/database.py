from pymongo import MongoClient


try:
    client = MongoClient("mongodb+srv://admin:adimn@cluster0.biz788r.mongodb.net/?retryWrites=true&w=majority")

    db = client.TODO_FASTAPI

    collection_name = db["todo_collection"]

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
