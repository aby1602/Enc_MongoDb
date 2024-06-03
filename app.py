from pymongo import MongoClient

# MongoDB connection URI
client = MongoClient("mongodb://admin:password@192.168.49.2:32000/")

# Select the database
db = client.mydatabase

# Select the collection
collection = db.mycollection

# Insert a document
document = {"name": "John Doe", "email": "john@example.com"}
collection.insert_one(document)

# Retrieve and print documents
for doc in collection.find():
    print(doc)
