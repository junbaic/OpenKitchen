from flask import Blueprint
from flask_restx import Api
from .controller.user import user_namespace
from .controller.recipe import recipe_namespace

blueprint = Blueprint("api", __name__)

api = Api(
  blueprint, 
  title="OpenKitchen backend",
  version="1.0",
  description="This is OpenKitchen backend api"
)

api.add_namespace(user_namespace, "/user")
api.add_namespace(recipe_namespace, "/recipe")