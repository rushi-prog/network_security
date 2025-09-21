from pymongo import MongoClient
client = MongoClient("mongodb+srv://username:password@cluster0.mongodb.net/test")

url = "mongodb+srv://opqp:Admin123@cluster0.pzi7yic.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(url)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)