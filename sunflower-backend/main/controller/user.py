from flask_restx import Namespace, Resource
from ..service.user import *
from flask import request

user_namespace = Namespace("User", description="User api")

# User register
@user_namespace.route("/register")
class UserRegister(Resource):
  @staticmethod
  def post():
    return process_register(request)

# User log in
@user_namespace.route("/login")
class UserLogin(Resource):
  @staticmethod
  def post():
    return process_login(request)

# Get user information
@user_namespace.route("/getUesrInfo")
class GetUserinfo(Resource):
  @staticmethod
  def get():
    return process_get_user_info(request)

# Modify user information
@user_namespace.route("/modifyProfile")
class GetUserinfo(Resource):
  @staticmethod
  def put():

    return process_modify_profile(request)

# User log out
@user_namespace.route("/logout")
class GetUserinfo(Resource):
  @staticmethod
  def put():
    return process_logout()

# Following user
# The username of the token is the logged-in person who chooses whether to toggle off or
# not when viewing another person's home page
@user_namespace.route("/followingUser")
class GetUserinfo(Resource):
  @staticmethod
  def put():
    return process_following_user(request)





















