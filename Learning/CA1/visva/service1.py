from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

users = {}
current_id = 1


@app.route("/users", methods=["POST"])
def create_user():
    global current_id
    logging.info("Create user request received")
    data = request.json
    user = {
        "id": current_id,
        "name": data["name"]
    }
    users[current_id] = user
    current_id += 1
    logging.info("User created")
    return jsonify(user)


@app.route("/users", methods=["GET"])
def get_users():
    logging.info("Get users request received")
    return jsonify(list(users.values()))


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    logging.info("Update user request received")
    if user_id in users:
        data = request.json
        users[user_id]["name"] = data["name"]
        logging.info("User updated")
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    logging.info("Delete user request received")
    if user_id in users:
        deleted = users.pop(user_id)
        logging.info("User deleted")
        return jsonify(deleted)
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(port=5001)
