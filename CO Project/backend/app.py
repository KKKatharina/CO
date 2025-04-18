from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/message")
def get_message():
    return jsonify({"msg": "Hello from Flask API!"})

if __name__ == "__main__":
    app.run(debug=True)
