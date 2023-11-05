import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/") 

db = client["mydatabase"] 

collection = db["mycollection"]  

data = {
    "name": "John",
    "age": 30
}

inserted_document = collection.insert_one(data)
print("Inserted document ID:", inserted_document.inserted_id)


for document in collection.find():
    print(document)


query = {"name": "John"}
new_values = {"$set": {"age": 31}}
collection.update_one(query, new_values)

updated_document = collection.find_one(query)
print("Updated document:", updated_document)

collection.delete_one(query)

client.close()
