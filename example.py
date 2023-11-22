## Render, Github, Flask and DialogFlow integration Example.
from flask import Flask, request, jsonify

import os

# Determine environment
prod = True if os.environ.get("PRODUCTION") == "production" else False

app = Flask(__name__)


@app.route("/test", methods=["POST"])
def example_route():
    data = request.get_json(silent=True)

    # Return request to client
    return jsonify(data)


if __name__ == "__main__":
    if prod:
        app.run()
    else:
        app.run(debug=True, host="127.0.0.1", port=8080)
