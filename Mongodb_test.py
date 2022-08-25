from pymongo import MongoClient

url = "mongodb+srv://pytech:admin@csd.j0wjc.mongodb.net/pytech?retryWrites=true&w=majority"client = MongoClient(url)db = client.pytech
