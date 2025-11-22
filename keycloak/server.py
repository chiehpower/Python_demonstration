import os
import time
from flask import Flask, request, jsonify
import cv2
import numpy as np
from keycloak import KeycloakOpenID

app = Flask(__name__)
_keycloak_client = None


def get_keycloak_client():
    """Lazily create a KeycloakOpenID client using env vars."""
    global _keycloak_client
    if _keycloak_client is None:
        server_url = os.getenv("KEYCLOAK_SERVER_URL", "http://127.0.0.1:8080/")
        realm = os.getenv("KEYCLOAK_REALM", "master")
        client_id = os.getenv("KEYCLOAK_CLIENT_ID", "admin-cli")
        client_secret = os.getenv("KEYCLOAK_CLIENT_SECRET")
        verify = os.getenv("KEYCLOAK_VERIFY", "false").lower() == "true"
        _keycloak_client = KeycloakOpenID(
            server_url=server_url,
            realm_name=realm,
            client_id=client_id,
            client_secret_key=client_secret,
            verify=verify,
        )
    return _keycloak_client


@app.route('/token', methods=['POST'])
def get_token():
    payload = request.get_json(silent=True) or {}
    username = payload.get("username")
    password = payload.get("password")
    app.logger.info(f"Received token request for username: {username}")
    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400
    try:
        app.logger.info(f"hi")
        kc = get_keycloak_client()
        app.logger.info(f"hi1")
        token = kc.token(username=username, password=password)
        app.logger.info(f"Token: {token}")
        return jsonify(token)
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": "failed to get token", "detail": str(exc)}), 500


if __name__ == '__main__':
    # This is used when running locally.
    app.run(host='0.0.0.0', port=5001, debug=True)
