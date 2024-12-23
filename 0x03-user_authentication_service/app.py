#!/usr/bin/env python3
""" basic flask app """

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/users", methods=['POST'])
def users():
    """
    register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        usr = AUTH.register_user(email, password)
        if usr is not None:
            return jsonify({
                "email": usr.email,
                "message": "user created"})
    except ValueError as e:
        return jsonify({"message": "email alredy registered"}), 400


@app.route("/")
def hello_world():
    """ basic function """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
