from flask_restx import fields

from app.api.blueprints.auth_management import auth_management_api


user_model = auth_management_api.model("User", {
    "id": fields.Integer(description="The user's id generated by the server"),
    "full_name": fields.String(description="The user's full name registred into the server"),
    "username": fields.String(description="The user's username registred into the server"),
    "email": fields.String(description="The user's main email registred into the server"),
    "phone": fields.String(description="The user's phone number registred into the server"),
})


register_user_model = auth_management_api.model("RegisterUser", {
    "full_name": fields.String(description="The user's full name", required=True),
    "username": fields.String(description="The user's username into the server", required=True),
    "email": fields.String(description="The user's main email", required=True),
    "phone": fields.String(description="The user's phone number email", required=False),
    "password": fields.String(description="The user's password to access the server", required=True),
})


edit_user_model = auth_management_api.model("EditUser", {
    "id": fields.Integer(description="The user's id generated by the server", required=True),
    "username": fields.String(description="The user's username registred into the server", required=False),
    "email": fields.String(description="The user's main email registred into the server", required=False),
    "phone": fields.String(description="The user's phone number registred into the server", required=False),
    "password": fields.String(description="The user's password to access the server", required=False),
})


authenticate_user_model = auth_management_api.model("AuthenticateUser", {
    "username": fields.String(description="The user's username registred into the server", required=True),
    "password": fields.String(description="The user's password to access the server", required=True),
})