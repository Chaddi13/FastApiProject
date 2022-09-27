from pymongo import MongoClient

# MongoDB connection

cluster = MongoClient("mongodb+srv://Chaddi:wfii123098@cluster0.q4d5v9j.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Parsing"]
collection = db["ParseCollection"]
