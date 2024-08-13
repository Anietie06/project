from pymongo import MongoClient
from pymongo.errors import ConnectionError
import time

def connect_to_mongo():
    client = None
    while client is None:
        try:
            # Attempt to connect to the MongoDB server
            client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
            # Test the connection
            client.admin.command('ping')
            print("Connected to MongoDB!")
        except ConnectionError:
            # Connection failed; wait and retry
            print("Failed to connect to MongoDB. Retrying in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying
    return client



# # Example operation: Insert a document
# document = {'name': 'Alice', 'age': 30}
# collection.insert_one(document)

# # Query the collection
# result = collection.find_one({'name': 'Alice'})
# print(result)
