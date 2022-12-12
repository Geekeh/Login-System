from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

mongo_url = 'mongo connection url'
database = MongoClient(mongo_url)
db = database['database_name']
collection = db['collection_name']


@app.route('/')
def index():
  return 'use /api'


@app.route("/api", methods=["POST", "GET"])
def api_page():
    if request.method == "POST":
        headers = request.headers
        if "key" not in headers or "hwid" not in headers:
            return ({"error": "invalid headers"})

        user_key = request.headers.get("key")
        database = collection.find()
        all_keys = []

        for x in database:
            all_keys.append(x['key'])

        if user_key not in all_keys:
            return ({"error": "invalid key"})

        key_info = collection.find_one({"key": user_key})
        if headers.get('hwid') == key_info['hwid']:
            key_info = collection.find_one({"key": user_key})
            return ({
                "valid_key": user_key,
                "hwid": headers.get('hwid'),
                "ip": key_info['ip']
            })
        else:
            return ({"error": "invalid headers"})
    else:
        return "invalid method used"


app.run(host='0.0.0.0', port=81)
