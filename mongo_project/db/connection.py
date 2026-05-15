from pymongo import MongoClient

USERNAME = "admin"
PASSWORD = "super_secure_password"
HOST = "localhost"
PORT = "27017"

uri = f"mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/"

client = MongoClient(uri)
db = client["myapp"]