from flask import Flask, request

app = Flask(__name__)

keys = ['123']

@app.route('/')
def index():
    return 'use /api'

@app.route("/api", methods=["POST", "GET"])
def api_page():
    if request.method == "POST":
        headers = request.headers
        if "key" not in headers:
            return ({"error":"invalid headers"})

        user_keys = request.headers.get('key')
        if user_keys not in keys:
            return ({"error": "invalid key"})
        return ({"valid key":user_keys})
    else:
        return "404 not found"


app.run(host='0.0.0.0', port=81)
