from flask import Flask, request, jsonify
from flask_cors import CORS
import routeros_api

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "app": "WIFI VOUCHER AI",
        "backend": "Siap"
    })

@app.route("/api/router/connect", methods=["POST"])
def connect_router():
    data = request.json or {}

    try:
        connection = routeros_api.RouterOsApiPool(
            data["ip"],
            username=data["username"],
            password=data["password"],
            port=int(data.get("port", 8728)),
            plaintext_login=True
        )

        api = connection.get_api()

        identity = api.get_resource(
            "/system/identity"
        ).get()

        connection.disconnect()

        return jsonify({
            "success": True,
            "message": "MikroTik berhasil terhubung",
            "identity": identity
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
