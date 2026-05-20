from pymongo import MongoClient

client = MongoClient(
    "mongodb://admin:super_secure_password@localhost:27017/admin"
)
db = client["biblioteca"]
libri = db["libri"]