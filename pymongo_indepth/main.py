import pymongo
# Connect to MongoDB instance running on localhost
client = pymongo.MongoClient()

#Create a Database called mydatabase
mydb = client["mydatabase"]
#Print the list of databases
print(client.list_database_names())

#mydatabase will not appear in the list
#MongoDB waits until you have created a collection with
#at least one document (record) before it actually
#creates the database

#Create a collection
mycol = mydb["people"]

#Insert a document into the collection
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

#Print the _id of the inserted document
print(x.inserted_id)