from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# MongoDB connection

# cluster = MongoClient("mongodb+srv://Chaddi:wfii123098@cluster0.q4d5v9j.mongodb.net/?retryWrites=true&w=majority")
# db = cluster["Parsing"]
# collection = db["ParseCollection"]

# if __name__ == '__main__':
#     uvicorn.run("main:app")
