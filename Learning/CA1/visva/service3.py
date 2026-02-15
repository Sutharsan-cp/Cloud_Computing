from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

USER_SERVICE = "http://localhost:5001"
LOG_SERVICE = "http://localhost:5002"


@app.route("/users", methods=["POST"])
def create_user():
    logging.info("Client requested create user")

    response = requests.post(f"{USER_SERVICE}/users", json=request.json)

    requests.post(f"{LOG_SERVICE}/log", json={"action": "create_user"})

    logging.info("Response returned to client")
    return jsonify(response.json())


@app.route("/users", methods=["GET"])
def get_users():
    logging.info("Client requested get users")

    response = requests.get(f"{USER_SERVICE}/users")

    requests.post(f"{LOG_SERVICE}/log", json={"action": "get_users"})

    logging.info("Response returned to client")
    return jsonify(response.json())


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    logging.info("Client requested update user")

    response = requests.put(
        f"{USER_SERVICE}/users/{user_id}",
        json=request.json
    )

    requests.post(f"{LOG_SERVICE}/log", json={"action": "update_user"})

    logging.info("Response returned to client")
    return jsonify(response.json())


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    logging.info("Client requested delete user")

    response = requests.delete(f"{USER_SERVICE}/users/{user_id}")

    requests.post(f"{LOG_SERVICE}/log", json={"action": "delete_user"})

    logging.info("Response returned to client")
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(port=5000)
