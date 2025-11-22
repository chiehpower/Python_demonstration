import argparse
import os
import sys
import requests


def get_token(username: str, password: str, base_url: str) -> dict:
    url = base_url.rstrip("/") + "/token"
    response = requests.post(url, json={"username": username, "password": password}, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    parser = argparse.ArgumentParser(description="Fetch Keycloak token via local Flask app")
    parser.add_argument("--url", default=os.getenv("APP_BASE_URL", "http://app:5001"), help="Base URL of the Flask app")
    parser.add_argument("--username", default="chieh", help="Keycloak username")
    parser.add_argument("--password",  default="chieh", help="Keycloak password")
    args = parser.parse_args()

    try:
        token = get_token(args.username, args.password, args.url)
        print(token)
    except requests.HTTPError as exc:
        print(f"Request failed: {exc} | response={exc.response.text if exc.response else 'n/a'}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
