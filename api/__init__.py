from flask_restx import Api
from api.auth import authorizations


api = Api(
    title="API Authentication Management",
    version="1.0",
    description="A secure Flask API that requires user authentication and manages access",
    authorizations=authorizations,
)
