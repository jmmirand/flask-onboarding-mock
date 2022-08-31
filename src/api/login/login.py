"""API Login."""
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_restx import Namespace, Resource, fields

api = Namespace("/", description="login")

mod_login_user_password = api.model(
    "login_user_password.",
    {
        "username": fields.String(required=True, description="UserName"),
        "password": fields.String(required=True, description="UserName"),
    },
)


@api.route("/login")
class api_login(Resource):
    """Login User and Password."""

    @api.doc("Login User/Password")
    @api.doc(body=mod_login_user_password)
    def post(self):
        """Login usuario y Password."""
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "test" or password != "test":
            response = jsonify({"msg": "Bad username or password"})
            response.status_code = 401
            return response
        iCont = 0
        claimData = {}
        while iCont < 2:
            key = "Key" + str(iCont)
            valor = "Valor que estoy recuperando - " + str(iCont)
            claimData[key] = valor
            iCont = iCont + 1

        access_token = create_access_token(identity=username, additional_claims=claimData)
        return jsonify(access_token=access_token)
