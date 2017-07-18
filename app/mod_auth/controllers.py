# Import flask dependencies
from flask import Blueprint, jsonify, request
from .services.UserService import UserService

import json
from bson import json_util

# Create a module / component
mod_auth = Blueprint("mod_auth", __name__, url_prefix="/auth")


@mod_auth.route("/signin", methods=['GET'])
def retrieve_account():
    users = UserService.retrieve_users()
    users_json = [json.dumps(user, default=json_util.default) for user in users]

    return jsonify(users_json)


@mod_auth.route("/signin", methods=['POST'])
def signin():
    UserService.registry_user(request.json)

    return jsonify({"success": True})
