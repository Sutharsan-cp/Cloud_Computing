from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

logs = []


@app.route("/log", methods=["POST"])
def add_log():
    logging.info("Log received")
    data = request.json
    logs.append(data)
    return jsonify({"status": "log stored"})


@app.route("/logs", methods=["GET"])
def get_logs():
    logging.info("Logs requested")
    return jsonify(logs)


if __name__ == "__main__":
    app.run(port=5002)
