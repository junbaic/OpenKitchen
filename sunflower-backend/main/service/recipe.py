from ..table.mytable import *
from flask import jsonify, make_response
from ..util import *
from collections import defaultdict

def process_get_all_recipes_brief_info(request):
  try:
    token_user_get = request.headers.get('Authorization')
    recipes_dict = defaultdict(lambda:dict())
    recipes_all = Recipe.query.all()
    # get name and time from token
    # if token_user_get is not none, means the user has logged in 
    if token_user_get:
      rq_username = decode_token(token_user_get).get('user_name')
      if User.query.filter(User.username==rq_username).first() == None:
        return make_response(jsonify(msg="token is not right"), 400) 

      if User.query.filter(User.username==rq_username).first().like:
        like_list = [int(each) for each in User.query.filter(User.username==rq_username).first().like.split(';')]
      else:
        like_list = []

      # following
      if User.query.filter(User.username == rq_username).first().following:
        following_user_list = [int(each) for each in
                              User.query.filter(User.username == rq_username).first().following.split(';')]
      else:
        following_user_list = []

    for each in recipes_all:
      username = User.query.filter(User.id == each.user_id).first().username
      recipes_dict[each.id]['recipe_id'] = each.id
      recipes_dict[each.id]['create_time'] = each.create_time
      recipes_dict[each.id]['contributor_id'] = each.user_id
      recipes_dict[each.id]['contributor'] = username
      recipes_dict[each.id]['name'] = each.name
      recipes_dict[each.id]['meal_type'] = each.meal_type
      recipes_dict[each.id]['picture'] = each.picture
      if token_user_get:
        recipes_dict[each.id]['like'] = 'no'
        for index in like_list:
          if index == each.id:
            recipes_dict[each.id]['like'] = 'yes'

      # following
      if token_user_get:
        # user = [1;2;4;5] recipe id = [1;3;4;5;6]
        # user = [1;3;5] recipe id = [2;3;5]
        user_recipe_id = []
        for user_id in following_user_list:
          recipe_all = Recipe.query.filter(Recipe.user_id == user_id).all()
          for recipe in recipe_all:
            user_recipe_id.append(recipe.id)
        recipes_dict[each.id]['following'] = 'no'
        for index in user_recipe_id:
          if index == each.id:
            recipes_dict[each.id]['following'] = 'yes'
          
    # sort by create time
    recipes_return = sorted(recipes_dict.values(), key=lambda x:x["create_time"], reverse=False)
    return make_response(jsonify(msg = "GET RECIPE BRIEF INFO SUCESS", recipe_briefInfo = recipes_return), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_get_following_recipe(request):
  try:
    # get username from token and look for following
    token_user_get = request.headers.get('Authorization')
    rq_username = decode_token(token_user_get).get('user_name')
    # like
    if User.query.filter(User.username==rq_username).first().like:
      like_list = [int(each) for each in User.query.filter(User.username==rq_username).first().like.split(';')]
    else:
      like_list = []
    # following
    if User.query.filter(User.username == rq_username).first().following:
        following_user_list = [int(each) for each in
                              User.query.filter(User.username == rq_username).first().following.split(';')]
    else:
        following_user_list = []
    
    # get name and time
    token_decode = decode_token(token_user_get)
    user_name = token_decode.get('user_name')
    following_user = User.query.filter(User.username == user_name).first().following
    
    if not following_user:
      return make_response(jsonify(msg = "Current user does not follow anyone"), 200)

    # 1. get all following users and store them in a list
    each_user = following_user.split(';')

    # 2. search each user id, and find their recipe id in recipe, store them as dictionary
    list_following_recipe = []
    for user_id in each_user:
        user_recipe = Recipe.query.filter(Recipe.user_id == user_id).all()
        for each in user_recipe:
          list_following_recipe.append(each.id)

    # 3. get all recipes id, and search for recipe info, store in list
    recipes_dict = defaultdict(lambda: dict())
    for following_recipe_id in list_following_recipe:
        recipes = Recipe.query.filter(Recipe.id == following_recipe_id).first()
        username = User.query.filter(User.id == recipes.user_id).first().username
        recipes_dict[following_recipe_id]['recipe_id'] = following_recipe_id
        recipes_dict[recipes.id]['create_time'] = recipes.create_time
        recipes_dict[recipes.id]['contributor_id'] = recipes.user_id
        recipes_dict[recipes.id]['contributor'] = username
        recipes_dict[recipes.id]['name'] = recipes.name
        recipes_dict[recipes.id]['meal_type'] = recipes.meal_type
        recipes_dict[recipes.id]['picture'] = recipes.picture
        recipes_dict[recipes.id]['like'] = 'no'
        recipes_dict[recipes.id]['following'] = 'no'

        for index in like_list:
          if index == recipes.id:
            recipes_dict[recipes.id]['like'] = 'yes'
        
        # following
        user_recipe_id = []
        for user_id in following_user_list:
            recipe_all = Recipe.query.filter(Recipe.user_id == user_id).all()
            for recipe in recipe_all:
                user_recipe_id.append(recipe.id)
        for index in user_recipe_id:
            if index == recipes.id:
                recipes_dict[recipes.id]['following'] = 'yes'
        
    following_recipes_return = sorted(recipes_dict.values(), key=lambda x: x["create_time"], reverse=False)
    return make_response(jsonify(msg="GET FOLLOWING RECIPES SUCESS", recipe_briefInfo=following_recipes_return), 200)
  except Exception as e:
      print(e)
      return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_like_recipe(request):
  try:
    # get token
    token_user_get = request.headers.get('Authorization')
    if token_user_get:
      # get username from token
      rq_username = decode_token(token_user_get).get('user_name')
      if User.query.filter(User.username==rq_username).first() == None:
        return make_response(jsonify(msg="token is not right"), 400)
      else:
        rq_recipe_id = request.get_json().get("recipe_id")
        if not rq_recipe_id:
          return make_response(jsonify(msg="Lack of recipe id, please send correct recipe id"), 400)
        else:
          if User.query.filter(User.username==rq_username).first().like:
            like_list = [int(each) for each in User.query.filter(User.username==rq_username).first().like.split(';')]
          else:
            like_list = []
          # like the recipe
          if rq_recipe_id not in like_list:
            like_list.append(rq_recipe_id)
            like_list = [str(each) for each in sorted(like_list, reverse=False)]
            like_insert = ";".join(like_list)
            User.query.filter(User.username==rq_username).update({"like": like_insert})
            db.session.commit()
            return make_response(jsonify(msg="Congratuations! You have liked this recipe!"), 200)
          else:# dislike the recipe
            like_list.remove(int(rq_recipe_id))
            like_list = [str(each) for each in sorted(like_list, reverse=False)]
            like_insert = ";".join(like_list)
            User.query.filter(User.username==rq_username).update({"like": like_insert})
            db.session.commit()
            return make_response(jsonify(msg="Congratuations! You have disliked this recipe!"), 200)
    else:
      return make_response(jsonify(msg="Lack of the token"), 400)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_create_recipe(request):
  try:
    token_get = request.headers.get('Authorization')
    recipe_info_get = request.get_json()

    # get username from token
    token_decode = decode_token(token_get)

    # verify necessary data
    user_id = User.query.filter(User.username==token_decode.get('user_name')).first().id
    rq_recipe_name = recipe_info_get.get("name")
    rq_method = recipe_info_get.get("method")
    rq_ingredients = recipe_info_get.get("ingredients")
    rq_picture = recipe_info_get.get("picture")
    rq_meal_type = recipe_info_get.get("meal_type")
    rq_create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not all([rq_ingredients, rq_recipe_name, rq_method, rq_picture, rq_meal_type]):
      return make_response(jsonify(msg = "Incomplete parameters"), 400)

    # finish check, insert data
    recipe_new = Recipe(
      user_id = user_id,
      name = rq_recipe_name,
      picture = rq_picture,
      meal_type = rq_meal_type,
      create_time = rq_create_time,
    )
    db.session.add(recipe_new )
    db.session.commit()

    # handle with Recipe_Ingredient
    # use user_id, name, create_time as query condition
    recipe_id = Recipe.query.filter(Recipe.user_id ==user_id, Recipe.name==rq_recipe_name, Recipe.create_time==rq_create_time).first().id
    for each in rq_ingredients:
      ingredient_new = Recipe_Ingredient(
        id_recipe = recipe_id,
        ingredient_name = each.get("ingredient_name"),
        ingredient_num = each.get("ingredient_num"),
        ingredient_unit = each.get("ingredient_unit"),
      )
      db.session.add(ingredient_new)
      db.session.commit()

    # handle with Recipe_Method
    for each in rq_method:
      method_new = Recipe_Method(
        id_recipe = recipe_id,
        method_step = each.get("method_step"),
        method_content = each.get("method_content"),
        method_photo = each.get("method_photo"),
        method_photo_file_name = each.get("method_photo_file_name")
      )
      db.session.add(method_new)
      db.session.commit()
    return make_response(jsonify(msg = "CREATE RECIPE SUCESS"), 200)

  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_update_recipe(request):
  try:
    token_get = request.headers.get('Authorization')
    recipe_info_get = request.get_json()
    # get username form token
    token_decode = decode_token(token_get)

    # verify token
    if User.query.filter(User.username==token_decode.get('user_name')).first()==None:
      return make_response(jsonify(msg = "Invalid token!"), 400)

    # verify necessary data
    user_id = User.query.filter(User.username==token_decode.get('user_name')).first().id
    rq_recipe_id = recipe_info_get.get("recipe_id")
    rq_name = recipe_info_get.get("name")
    rq_method = recipe_info_get.get("method")
    rq_ingredients = recipe_info_get.get("ingredients")
    rq_picture = recipe_info_get.get("picture")
    rq_meal_type = recipe_info_get.get("meal_type")
    rq_update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not all([rq_ingredients, rq_name, rq_method, rq_picture, rq_meal_type]):
      return make_response(jsonify(msg = "Incomplete parameters"), 400)

    # verify recipe existence
    if Recipe.query.filter(Recipe.id==rq_recipe_id).first()==None:
      return make_response(jsonify(msg = "Error recipe id, this recipe does not exist!"), 400)

    # verify if update recipe belongs to current user
    if Recipe.query.filter(Recipe.user_id==user_id, Recipe.id==rq_recipe_id).first() == None:
      return make_response(jsonify(msg = "Error, update data does not belongs to current user"), 400)

    # update data in Recipe
    Recipe.query.filter(Recipe.user_id==user_id, Recipe.id==rq_recipe_id).update({
      'user_id' : user_id,
      'name' : rq_name,
      'picture' : rq_picture,
      'meal_type' : rq_meal_type,
      'create_time' : rq_update_time,
    })
    db.session.commit()

    # handle with recipe_ingredients
    # use user_id, name, create_time as query condition
    # recipe_id = Recipe.query.filter(Recipe.user_id ==user_id, Recipe.id==rq_recipe_id, Recipe.create_time==rq_update_time).first().id
    # delete previous ingerdient
    Recipe_Ingredient.query.filter(Recipe_Ingredient.id_recipe == rq_recipe_id).delete()
    db.session.commit()
    for each in rq_ingredients:
      ingredient_new = Recipe_Ingredient(
        id_recipe = rq_recipe_id,
        ingredient_name = each.get("ingredient_name"),
        ingredient_num = each.get("ingredient_num"),
        ingredient_unit = each.get("ingredient_unit"),
      )
      db.session.add(ingredient_new)
      db.session.commit()

    # handle with Recipe_Method
    # delete privious method
    Recipe_Method.query.filter(Recipe_Method.id_recipe == rq_recipe_id).delete()
    for each in rq_method:
      method_new = Recipe_Method(
        id_recipe = rq_recipe_id,
        method_step = each.get("method_step"),
        method_content = each.get("method_content"),
        method_photo = each.get("method_photo"),
        method_photo_file_name = each.get("method_photo_file_name")
      )
      db.session.add(method_new)
      db.session.commit()
    return make_response(jsonify(msg = "UPDATE RECIPE SUCESS"), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_delete_recipe(request, recipe_id):
  try:
    token_get = request.headers.get('Authorization')
    # get user name from token
    token_decode = decode_token(token_get)
    rq_recipe_id = recipe_id

    # verify necessary data
    if rq_recipe_id == None:
      return make_response(jsonify(msg = "Lack recipe id"), 400)

    # verify if delete recipe belongs to current user
    user_id = User.query.filter(User.username==token_decode.get('user_name')).first().id
    if Recipe.query.filter(Recipe.user_id==user_id, Recipe.id==rq_recipe_id).first() == None:
      return make_response(jsonify(msg = "Error, delete recipe does not belongs to current user"), 400) 
    
    recipe_id = Recipe.query.filter(Recipe.user_id==user_id, Recipe.id==rq_recipe_id).first().id
    
    # use user_id and name as query
    Recipe.query.filter(Recipe.user_id==user_id, Recipe.id==recipe_id).delete()
    db.session.commit()

    Recipe_Ingredient.query.filter(Recipe_Ingredient.id==recipe_id).delete()
    db.session.commit()

    Recipe_Method.query.filter(Recipe_Method.id==recipe_id).delete()
    db.session.commit()

    return make_response(jsonify(msg = "DELETE RECIPE SUCESS"), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_get_detail_info_recipe(request, recipe_id):
  try:
    token_get = request.headers.get('Authorization')
    token_decode = decode_token(token_get)
    # verify token
    if token_get==None or User.query.filter(User.username==token_decode.get('user_name')).first() == None:
      return make_response(jsonify(msg = "Invalid token"), 400)

    rq_recipe_id  = recipe_id
    if rq_recipe_id == None or rq_recipe_id == " ":
      return make_response(jsonify(msg = "Imcomplete parameters"), 400)

    # verify recipe existence
    if Recipe.query.filter(Recipe.id==rq_recipe_id).first()==None:
      return make_response(jsonify(msg = "Incorrect recipe id, this recipe does not exist"), 400)
    else:
      response_dict = defaultdict(lambda:dict())
      recipe_query = Recipe.query.filter(Recipe.id==rq_recipe_id).first()
      
      response_dict["recipe_name"] = recipe_query.name
      response_dict["contributor"] = User.query.filter(User.id==recipe_query.user_id).first().username
      response_dict["recipe_picture"] = recipe_query.picture
      response_dict["meal_type"] = recipe_query.meal_type
      response_dict["create_time"] = recipe_query.create_time
      if User.query.filter(User.username==token_decode.get('user_name')).first().tried == None:
        response_dict["tried"] = False
      else:
        tried_list = User.query.filter(User.username==token_decode.get('user_name')).first().tried.split(';')
        if rq_recipe_id not in tried_list:
          response_dict["tried"] = False
        else:
          response_dict["tried"] = True


      ingredient_query = recipe_query.ingredients
      response_dict["ingredients"] = []

      methods_query = recipe_query.methods
      response_dict["methods"] = []


      if ingredient_query:
        for each in ingredient_query:
          ingredient = {}
          ingredient["ingredient_name"] = each.ingredient_name
          ingredient["ingredient_num"] = each.ingredient_num
          ingredient["ingredient_unit"] = each.ingredient_unit
          response_dict["ingredients"].append(ingredient)
      
      if methods_query:
        for each in methods_query:
          method = {}
          method["method_step"] = each.method_step
          method["method_content"] = each.method_content
          method["method_photo"] = each.method_photo
          method["method_photo_file_name"] = each.method_photo_file_name
          response_dict["methods"].append(method)
      return make_response(jsonify(msg = "SUCCESS", data = response_dict), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_get_recipe_comment(recipe_id):
  try:
    rq_recipe_id  = recipe_id
    if rq_recipe_id == None or rq_recipe_id == " ":
      return make_response(jsonify(msg = "Imcomplete parameters"), 400)

    # verify recipe existence
    if Recipe.query.filter(Recipe.id==rq_recipe_id).first()==None:
      return make_response(jsonify(msg = "Incorrect recipe id, this recipe does not exist"), 400)
    else:
      response_dict = defaultdict(lambda:dict())
      recipe_query = Recipe.query.filter(Recipe.id==rq_recipe_id).first()
      comment_query = recipe_query.comments
      if comment_query:
        for each in comment_query:
          response_dict[each.id]['comment_time']=each.comment_time
          response_dict[each.id]['comment_username']=each.comment_username
          response_dict[each.id]['content']=each.comment_content
      else:
        return make_response(jsonify(msg = "SUCCESS! Current recipe does not have any comment"), 200)
      
      # Sort comments in the order of nearest comment time
      response_dict = sorted(response_dict.values(), key=lambda x: x["comment_time"], reverse=True)
      return make_response(jsonify(msg = "SUCCESS", data = response_dict), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_rating_recipe(request):
  try:
    token_get = request.headers.get('Authorization')
    token_decode = decode_token(token_get)

    # verify token
    if token_get==None or User.query.filter(User.username==token_decode.get('user_name')).first() == None:
      return make_response(jsonify(msg = "Invalid token"), 400) 

    rating_info_get = request.get_json()
    
    # verify necessary data
    rq_recipe_id = rating_info_get.get("recipe_id")
    rq_rating = rating_info_get.get("rating")

    if not all([rq_recipe_id, rq_rating]):
      return make_response(jsonify(msg = "Incomplete parameters"), 400)

    rq_username =token_decode.get('user_name')
  
    # verify rating recipe existence
    if Recipe_Rating.query.filter(Recipe_Rating.id_recipe==rq_recipe_id).first()==None:
      return make_response(jsonify(msg = "This recipe does not exist in the database"), 200)

    # have rating before
    rating_query = Recipe_Rating.query.filter(Recipe_Rating.id_recipe==rq_recipe_id, Recipe_Rating.rating_username==rq_username)
    if rating_query.first():
      rating_query.update({
        'rating_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        'rating': rq_rating
      })
      db.session.commit()
    # haven't rating before
    elif rating_query.first()==None:
      rating_new = Recipe_Rating(
        id_recipe= rq_recipe_id,
        rating_time= datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        rating_username= rq_username,
        rating= rq_rating
      )
      db.session.add(rating_new)
      db.session.commit()

    return make_response(jsonify(msg="Rating SUCESS!"), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_get_recipe_average_rating(request, recipe_id):
  try:
    # acquire username from token
    token_get = request.headers.get('Authorization')
    token_decode = decode_token(token_get)
    username = token_decode.get('user_name')

    if token_get == None or User.query.filter(User.username == username).first() == None:
        return make_response(jsonify(msg="Invalid token"), 400)

    if Recipe_Rating.query.filter(Recipe_Rating.id_recipe == recipe_id).first() == None:
        return make_response(jsonify(msg="This recipe does not exist in the database"), 200)
    else:
        initial_rating = 0
        rating_number = 0
        rating_all = Recipe_Rating.query.filter(Recipe_Rating.id_recipe == recipe_id).all()
        for rating in rating_all:
            initial_rating += float(rating.rating)
            rating_number += 1
        # print(initial_rating)
        # print(rating_number)
        recipe_average_rating = '%.2f' % (initial_rating / rating_number)
        return make_response(jsonify(msg="Get recipe average rating successfully",
                      recipe_average_rating=recipe_average_rating), 200)

  except Exception as e:
      print(e)
      return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_search_recipe(request, keywords):
  try:
    token_user_get = request.headers.get('Authorization')
    # if token_user_get is not none, means the user has logged in 
    if token_user_get:
      rq_username = decode_token(token_user_get).get('user_name')
      # verify token
      if User.query.filter(User.username==rq_username).first() == None:
        return make_response(jsonify(msg="token is not right"), 400)
      
      if User.query.filter(User.username==rq_username).first().like:
        like_list = [int(each) for each in User.query.filter(User.username==rq_username).first().like.split(';')]
      else:
        like_list = []

    recipes_dict = defaultdict(lambda:dict())

    # get the keywords of each query type
    rq_keywords = keywords.split('&')
    rq_keywords_ingredient = "none"
    rq_keywords_method = "none"
    rq_keywords_mealtype = "none"
    rq_keywords_recipename = "none"

    for each in rq_keywords:
      if "ingredient" in each:
        rq_keywords_ingredient = each.replace("ingredient:", "").replace(":", "").replace("<", "").replace(">", "").rstrip().lstrip()
      if "method" in each:
        rq_keywords_method = each.replace("method", "").replace(":", "").replace("<", "").replace(">", "").rstrip().lstrip()
      if "mealType" in each:
        rq_keywords_mealtype = each.replace("mealType", "").replace(":", "").replace("<", "").replace(">", "").rstrip().lstrip()
      if "recipeName" in each:
        rq_keywords_recipename = each.replace("recipeName", "").replace(":", "").replace("<", "").replace(">", "").rstrip().lstrip()

    list_ingredient, list_method, list_mealtype, list_recipename = [], [], [], []

    # do four queries in the database 
    query_ingredient = Recipe_Ingredient.query.filter(Recipe_Ingredient.ingredient_name.like(f'%{rq_keywords_ingredient}%')).all()
    query_method = Recipe_Method.query.filter(Recipe_Method.method_content.like(f'%{rq_keywords_method}%')).all()
    query_mealtype = Recipe.query.filter(Recipe.meal_type.like(f'%{rq_keywords_mealtype}%')).all()
    query_recipename = Recipe.query.filter(Recipe.name.like(f'%{rq_keywords_recipename}%')).all()

    for each in query_ingredient:
      if each.id_recipe not in list_ingredient:
        list_ingredient.append(each.id_recipe)
    
    for each in query_method:
      if each.id_recipe not in list_method:
        list_method.append(each.id_recipe)
    
    for each in query_mealtype:
      if each.id not in list_mealtype:
        list_mealtype.append(each.id)
    
    for each in query_recipename:
      if each.id not in list_recipename:
        list_recipename.append(each.id)
    
    list_all = [list_ingredient, list_method, list_mealtype, list_recipename]
    print(list_all)
    list_all = [x for x in list_all if x]
    
    # get the intersection recipe id of four queries
    if len(list_all) == 0:
      return make_response(jsonify(msg="Your retrieval keywords match nothing in the database!"), 200)
    elif len(list_all) == 1:
      list_final = list_all[0]
    else:
      list_final = set(list_all[0]).intersection(*list_all[1:])
    
    list_final = list(list_final)
    print(list_final)
    
    for each in list_final:
      recipe = Recipe.query.filter(Recipe.id==each).first()
      username = User.query.filter(User.id == recipe.user_id).first().username
      recipes_dict[each]['recipe_id'] = recipe.id
      recipes_dict[each]['create_time'] = recipe.create_time
      recipes_dict[each]['contributor_id'] = recipe.user_id
      recipes_dict[each]['contributor'] = username
      recipes_dict[each]['name'] = recipe.name
      recipes_dict[each]['meal_type'] = recipe.meal_type
      recipes_dict[each]['picture'] = recipe.picture
      if token_user_get:
        recipes_dict[each]['like'] = 'no'
        for index in like_list:
          if index == each:
            recipes_dict[each]['like'] = 'yes'
    recipes_return = sorted(recipes_dict.values(), key=lambda x:x["create_time"], reverse=False)
    return make_response(jsonify(msg = "Success! Get recipe brief info by recipe name!", recipe_briefInfo = recipes_return), 200)

  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_add_recipe_comments(request):
  try:
    # recipe_id, comment_username, comment_time, comment_content
    # acquire recipe_id，front-end need give some messages to back-end (recipe_id，comment_content)
    recipe_info_get = request.get_json()
    id_recipe = recipe_info_get.get("recipe_id")
    comment_content = recipe_info_get.get("comment_content")
    # print(id_recipe)
    # print(comment_content)
    # comment_time generated by back-end, comment_content acquired by front-end
    # comment_time:
    comment_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(comment_time)
    # comment_username: based on token to get user_name
    token_user_get = request.headers.get('Authorization')
    comment_username = decode_token(token_user_get).get('user_name')
    # print(comment_username)

    # insert new comment into Recipe_Comment table
    recipe_comment = Recipe_Comment(
        id_recipe=id_recipe,
        comment_time=comment_time,
        comment_username=comment_username,
        comment_content=comment_content
    )
    db.session.add(recipe_comment)
    db.session.commit()

    return make_response(jsonify(msg="ADD COMMENT SUCCESSFULLY"), 200)

  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400 ) 

def process_get_my_recipes(request):
  try:
    token_get = request.headers.get('Authorization')
    # Verify token existence
    if token_get==None or token_get=='':
      return make_response(jsonify(msg="Miss token!"), 400) 

    token_decode = decode_token(token_get)
    # Verify token
    if User.query.filter(User.username==token_decode.get('user_name')).first() == None:
      return make_response(jsonify(msg = "Invalid token"), 400)

    rq_username = token_decode.get('user_name')
    query_user = User.query.filter(User.username==rq_username).first()

    # Verify created recipes
    if query_user.recipes==[]:
      return make_response(jsonify(msg = "Success! But you haven't created any recipe before!"), 200)

    if User.query.filter(User.username==rq_username).first().like:
      like_list = [int(each) for each in User.query.filter(User.username==rq_username).first().like.split(';')]
    else:
      like_list = []

    recipes_dict = defaultdict(lambda:dict())

    for each_recipe in query_user.recipes:
      username = User.query.filter(User.id == each_recipe.user_id).first().username
      recipes_dict[each_recipe.id]['recipe_id'] = each_recipe.id
      recipes_dict[each_recipe.id]['create_time'] = each_recipe.create_time
      recipes_dict[each_recipe.id]['contributor_id'] = each_recipe.user_id
      recipes_dict[each_recipe.id]['contributor'] = username
      recipes_dict[each_recipe.id]['name'] = each_recipe.name
      recipes_dict[each_recipe.id]['meal_type'] = each_recipe.meal_type
      recipes_dict[each_recipe.id]['picture'] = each_recipe.picture
      if token_get:
          recipes_dict[each_recipe.id]['like'] = 'no'
          for index in like_list:
            if index == each_recipe.id:
              recipes_dict[each_recipe.id]['like'] = 'yes'

    recipes_return = sorted(recipes_dict.values(), key=lambda x:x["create_time"], reverse=False)
    
    return make_response(jsonify(msg = "Success!", my_recipes = recipes_return), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_get_my_tried_recipes(request):
  try:
    token_get = request.headers.get('Authorization')
    # Verify token existence
    if token_get==None or token_get=='':
      return make_response(jsonify(msg="Miss token!"), 400)

    token_decode = decode_token(token_get)
    # verify token
    if User.query.filter(User.username==token_decode.get('user_name')).first() == None:
      return make_response(jsonify(msg = "Invalid token"), 400)

    rq_username = token_decode.get('user_name')
    query_user = User.query.filter(User.username==rq_username).first()
    tried_list = query_user.tried
    if not tried_list:
      return make_response(jsonify(msg = "Success! But you haven't tried any recipes before!"), 200)
    tried_list = [int(_) for _ in tried_list.split(';')]
    
    if query_user.like:
      like_list = [int(each) for each in query_user.like.split(';')]
    else:
      like_list = []
    
    # following
    if query_user.following:
        following_user_list = [int(each) for each in query_user.following.split(';')]
    else:
        following_user_list = []

    recipes_dict = defaultdict(lambda:dict())

    for each_recipe_id in tried_list:
      each_recipe = Recipe.query.filter(Recipe.id==each_recipe_id).first()
      username = User.query.filter(User.id == each_recipe.user_id).first().username
      recipes_dict[each_recipe_id]['recipe_id'] = each_recipe_id
      recipes_dict[each_recipe_id]['create_time'] = each_recipe.create_time
      recipes_dict[each_recipe_id]['contributor_id'] = each_recipe.user_id
      recipes_dict[each_recipe_id]['contributor'] = username
      recipes_dict[each_recipe_id]['name'] = each_recipe.name
      recipes_dict[each_recipe_id]['meal_type'] = each_recipe.meal_type
      recipes_dict[each_recipe_id]['picture'] = each_recipe.picture
      recipes_dict[each_recipe_id]['like'] = 'no'
      recipes_dict[each_recipe_id]['following'] = 'no'
      for index in like_list:
        if index == each_recipe.id:
          recipes_dict[each_recipe.id]['like'] = 'yes'
      # following
      user_recipe_id = []
      for user_id in following_user_list:
          recipe_all = Recipe.query.filter(Recipe.user_id == user_id).all()
          for recipe in recipe_all:
              user_recipe_id.append(recipe.id)
      for index in user_recipe_id:
          if index == each_recipe.id:
              recipes_dict[each_recipe.id]['following'] = 'yes'

    recipes_return = sorted(recipes_dict.values(), key=lambda x:x["create_time"], reverse=False)
    return make_response(jsonify(msg = "Success!", my_recipes = recipes_return), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_get_recomended_recipes(recipe_id):
  try:
    rq_recipe = Recipe.query.filter(Recipe.id == recipe_id).first()
    if not rq_recipe:
        return make_response(jsonify(msg="This recipe does not exist, please change recipe id!"), 200)

    recommended_recipes_id = get_recommended_recipes_id(recipe_id, Recipe_Ingredient)
    recipes_dict = defaultdict(lambda: dict())
    for each in recommended_recipes_id:
      each_recipe_id = each[0]
      similarity = each[1]
      each_recipe = Recipe.query.filter(Recipe.id==each_recipe_id).first()
      username = User.query.filter(User.id == each_recipe.user_id).first().username
      recipes_dict[each_recipe_id]['recipe_id'] = each_recipe_id
      recipes_dict[each_recipe_id]['similarity'] = similarity
      recipes_dict[each_recipe_id]['create_time'] = each_recipe.create_time
      recipes_dict[each_recipe_id]['contributor_id'] = each_recipe.user_id
      recipes_dict[each_recipe_id]['contributor'] = username
      recipes_dict[each_recipe_id]['name'] = each_recipe.name
      recipes_dict[each_recipe_id]['meal_type'] = each_recipe.meal_type
      recipes_dict[each_recipe_id]['picture'] = each_recipe.picture
      recipes_dict[each_recipe_id]['like'] = 'no'
      recipes_dict[each_recipe_id]['following'] = 'no'
      for index in recommended_recipes_id:
        if index == each_recipe.id:
          recipes_dict[each_recipe.id]['like'] = 'yes'
    recipes_return = sorted(recipes_dict.values(), key=lambda x: x["similarity"], reverse=True)
    return make_response(jsonify(msg="Success!", my_recipes=recipes_return), 200)

  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)

def process_try_recipes(request):
  try:
    # verify token
    if not request.headers:
      return make_response(jsonify(msg="Lack of the token"), 400)
    
    token_user_get = request.headers.get('Authorization')
    if not token_user_get:
      return make_response(jsonify(msg="Lack of the token"), 400)
    
    if decode_token(token_user_get) == None:
      return make_response(jsonify(msg="Invalid token"), 400)

    rq_username = decode_token(token_user_get).get('user_name')
    if User.query.filter(User.username==rq_username).first() == None:
      return make_response(jsonify(msg="token is not right"), 400)
    # verify recipe id
    rq_recipe_id = request.get_json().get("recipe_id")
    if not rq_recipe_id:
      return make_response(jsonify(msg="Lack of recipe id, please send correct recipe id"), 400)

    if User.query.filter(User.username==rq_username).first().tried:
      tried_list = [int(each) for each in User.query.filter(User.username==rq_username).first().tried.split(';')]
    else:
      tried_list = []
    
    # Try the recipe
    if rq_recipe_id not in tried_list:
      if Recipe.query.filter(Recipe.id==rq_recipe_id).first()==None:
        return make_response(jsonify(msg="This recipe does not exist, please confirm recipe id!"), 400)
      tried_list.append(rq_recipe_id)
      tried_list = [str(each) for each in sorted(tried_list, reverse=False)]
      tried_insert = ";".join(tried_list)
      User.query.filter(User.username==rq_username).update({"tried": tried_insert})
      db.session.commit()
      return make_response(jsonify(msg="Congratuations! You have tried this recipe!"), 200)
    else:# untry the recipe
      tried_list.remove(int(rq_recipe_id))
      tried_list = [str(each) for each in sorted(tried_list, reverse=False)]
      tried_insert = ";".join(tried_list)
      User.query.filter(User.username==rq_username).update({"tried": tried_insert})
      db.session.commit()
      return make_response(jsonify(msg="Congratuations! You have untried this recipe!"), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify(msg="Error, please check if the access is correct"), 400)




