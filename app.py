import threading
from flask import Flask, jsonify, request
from config_loader import load_config, save_config, CONFIG_PATH

app = Flask(__name__)
_config_lock = threading.Lock()
config = load_config()

@app.route("/config", methods=["GET"])
def get_config():
    with _config_lock:
        return jsonify({
            "app": config.app.dict(),
            "network": config.network.dict(),
            "features": config.features.dict()
        })

@app.route("/toggle-feature/<feature_name>", methods=["POST"])
def toggle_feature(feature_name):
    global config
    with _config_lock:
        data = config.dict()
        features = data.setdefault("features", {})
        if feature_name not in features:
            return jsonify({"error": "feature not found"}), 404
        features[feature_name] = not features[feature_name]
        try:
            save_config(data, CONFIG_PATH)
            # reload validated config into memory
            config = load_config(CONFIG_PATH)
        except Exception as e:
            return jsonify({"error": f"failed to save or reload config: {e}"}), 500
    return jsonify({"feature": feature_name, "value": features[feature_name]})

@app.route("/reload-config", methods=["POST"])
def reload_config():
    global config
    with _config_lock:
        try:
            config = load_config(CONFIG_PATH)
        except Exception as e:
            return jsonify({"error": f"failed to reload config: {e}"}), 500
    return jsonify({"status": "reloaded", "app_mode": config.app.mode})

if __name__ == "__main__":
    app.run(host=config.network.host, port=config.network.port, debug=(config.app.mode != "production"))
