from ..table.mytable import *
from flask import jsonify, make_response
from datetime import datetime, timedelta
from .. import db
from ..util import *

# Register
def process_register(request):
  try:
    register_info = request.get_json() # get register info and transfer to json
    # get each data
    rq_username = register_info.get('username')
    rq_password = register_info.get('password')
    rq_email = register_info.get('email')
    

    # check necessary data
    if not all([rq_username, rq_password, rq_email]):
      return make_response(jsonify(msg = "Incomplete parameters"), 400)

    # check if current user has registered
    if User.query.filter(User.username==rq_username).first() != None:
      return make_response(jsonify(msg = "The user has registered"), 400)
    
    else:
      # finish checking, insert data
      user_new = User(
        username = rq_username,
        password = rq_password,
        email = rq_email,
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      )
      db.session.add(user_new)
      db.session.commit()

      new_user = User.query.filter(User.username==rq_username).first()
      token = generate_token(new_user.username)

      return make_response(jsonify(msg="REGISTER SUCCESS", username = rq_username, token=token),200)

  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

# Log in
def process_login(request):
  try:
    user_info_get = request.get_json()
    username = user_info_get.get("username")
    # check current user register
    if User.query.filter(User.username==username).first() == None:
      return make_response(jsonify(msg = "This user has not registered yet"), 400)
    else:
      # verify password
      password_get = user_info_get.get("password")
      password_store = User.query.filter(User.username==username).first().password
      if password_get != password_store:
        return make_response(jsonify(msg = "Incorrect password"), 400)
      else:
        token = generate_token(username)
        avatar = User.query.filter(User.username==username).first().avatar
        email = User.query.filter(User.username==username).first().email
        BIO = User.query.filter(User.username==username).first().BIO
        return make_response(jsonify(
            msg = "LOGIN SUCCESS", 
            username = username, 
            email = email,
            BIO = BIO,
            avatar = avatar,
            token=token
            ), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

# Get user information
def process_get_user_info(request):
  try:
    token_user_get = request.headers.get('Authorization')
    token_decode = decode_token(token_user_get)
    rq_username = token_decode.get('user_name')
    user_info = User.query.filter(User.username == rq_username).first()
    if not user_info:
      return make_response(jsonify(msg="We do not have information of the current user in the database"),200)

    return make_response(jsonify(
        username=user_info.username,
        password=user_info.password,
        avatar = user_info.avatar, 
        email = user_info.email,
        BIO = user_info.BIO,
      ),200)
  except Exception as e:
      print(e)
      return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

# Modify user information
def process_modify_profile(request):
  try:
      token_user_get = request.headers.get('Authorization')
      # get name and time from token
      token_decode = decode_token(token_user_get)
      # get all info
      modify_user_info = request.get_json()
      # only login sucess can modify user profile
      # can not modify user name

      # 1. can not find this user
      current_user = User.query.filter(User.username == token_decode.get('user_name')).first()
      # 2. can not modify username，return 400
      if token_decode.get('user_name') != modify_user_info.get('username'):
          return make_response(jsonify(msg='error: you cannot change your username, please make sure username and token are correct'), 400)
      else:
          # 3. modify password、avatar、email、BIO、create_time
          if modify_user_info.get('password'):
            current_user.password = modify_user_info['password']
          if modify_user_info.get('avatar'):
            current_user.avatar = modify_user_info['avatar']
          if modify_user_info.get('email'):
            current_user.email = modify_user_info['email']
          if modify_user_info.get('BIO'):
            current_user.BIO = modify_user_info['BIO']
          current_user.create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          # if modify_user_info.get('avatar'):
          #     curr_user.avatar = base64.b64decode(modify_user_info['avatar'])
      # 4. check necessary data
      if not all([current_user.password, current_user.avatar, current_user.email, current_user.BIO]):
          return make_response(jsonify(msg="Incomplete parameters"), 400)
      else:
          # finish check add data
          db.session.add(current_user)
          db.session.commit()

          return make_response(jsonify(msg="MODIFY SUCESS"), 200)

  except Exception as e:
      print(e)
      return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_logout():
  return make_response(jsonify(msg="LOG OUT SUCESS"), 200)

# following user
# The username of the token is the logged-in person who chooses whether to toggle off or
# not when viewing another person's home page
def process_following_user(request):
  try:
    # get token
    token_user_get = request.headers.get('Authorization')
    # get username from token and username is unique
    username = decode_token(token_user_get).get('user_name')
    if User.query.filter(User.username == username).first() == None:
        return make_response(jsonify(msg="token is not right"), 400)
    else:
        # front-end give a recipe_id to back-end
        front_recipe_id = request.get_json().get("recipe_id")
        print(front_recipe_id)
        if not front_recipe_id:
            return make_response(jsonify(msg="Lack of recipe id, please send correct recipe id"), 400)
        else:
            # finding author_id through the recipe_id
            author_id = Recipe.query.filter(Recipe.id == front_recipe_id).first().user_id
            if User.query.filter(User.username == username).first().following:
                following_user_list = [int(each) for each in
                                      User.query.filter(User.username == username).first().following.split(';')]
            else:
                following_user_list = []
            # following user
            if author_id not in following_user_list:
                following_user_list.append(author_id)
                following_user_list_new = [str(each) for each in sorted(following_user_list, reverse=False)]
                following_insert = ";".join(following_user_list_new)
                User.query.filter(User.username == username).update({"following": following_insert})
                db.session.commit()
                return make_response(jsonify(msg="You have successfully followed this author"), 200)
            # unfollowing user
            else:
                following_user_list.remove(int(author_id))
                following_user_list_new = [str(each) for each in sorted(following_user_list, reverse=False)]
                following_insert = ";".join(following_user_list_new)
                User.query.filter(User.username == username).update({"following": following_insert})
                db.session.commit()
                return make_response(jsonify(msg="You have successfully unfollowed this author"), 200)
  except Exception as e:
      print(e)
      return make_response(jsonify(msg="Error, please check if the access is correct"), 400)


