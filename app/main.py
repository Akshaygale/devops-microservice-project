from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="OK"), 200

@app.route("/info")
def info():
    return jsonify(
        app="DevOps Microservice",
        version="1.0",
        environment="production"
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
