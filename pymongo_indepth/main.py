import pymongo
# Connect to MongoDB instance running on localhost
client = pymongo.MongoClient()

#Create a Database called mydatabase
mydb = client["mydatabase"]
#Print the list of databases
print(client.list_database_names())