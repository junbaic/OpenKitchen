from flask_restx import Namespace, Resource
from ..service.recipe import *
from flask import request

recipe_namespace = Namespace("Recipe", description="Recipe api")



# Get all recipe brief infomation
@recipe_namespace.route("/getAllRecipesBriefInfo")
class GetAllRecipesBriefInfo(Resource):
  @staticmethod
  def get():
    return process_get_all_recipes_brief_info(request)

# Get all recipes from following contributors 
@recipe_namespace.route("/getFollowingRecipe")
class GetFollowingRecipe(Resource):
  @staticmethod
  def get():
    return process_get_following_recipe(request)

# Like or dislike a recipe
@recipe_namespace.route("/likeRecipe")
class LikeRecipe(Resource):
  @staticmethod
  def put():
    return process_like_recipe(request)
  
# Create a new recipe
@recipe_namespace.route("/createRecipe")
class CreateRecipe(Resource):
  @staticmethod
  def post():
    
    return process_create_recipe(request)

# Update recipe
@recipe_namespace.route("/updateRecipe")
class UpdateRecipe(Resource):
  @staticmethod
  def put():
    return process_update_recipe(request)

# Delete recipe
@recipe_namespace.route("/deleteRecipe/<recipe_id>")
class DeleteRecipe(Resource):
  @staticmethod
  def put(recipe_id):
    return process_delete_recipe(request, recipe_id)

# Get all detail info of a recipe
@recipe_namespace.route("/getRecipeDetailInfo/<recipe_id>")
class GetRecipeDetailInfo(Resource):
  @staticmethod
  def get(recipe_id):
    return process_get_detail_info_recipe(request, recipe_id)

# Get comments of current recipe
@recipe_namespace.route("/getRecipeComment/<recipe_id>")
class GetRecipeComment(Resource):
  @staticmethod
  def get(recipe_id):
    return process_get_recipe_comment(recipe_id)

# Rating for a recipe
@recipe_namespace.route("/ratingRecipe")
class RatingRecipe(Resource):
  @staticmethod
  def post():
    return process_rating_recipe(request)

# get a recipe average rating
@recipe_namespace.route("/getRecipeAverageRating/<recipe_id>")
class GetRecipeAverageRating(Resource):
  @staticmethod
  def get(recipe_id):
    return process_get_recipe_average_rating(request, recipe_id)

# Search recipe according to recipe_name, ingredient, contributor
@recipe_namespace.route("/searchRecipe/<keywords>")
class SearchRecipe(Resource):
  @staticmethod
  def get(keywords):
    return process_search_recipe(request, keywords)

# Add recipe comments
@recipe_namespace.route("/addRecipeComments")
class AddRecipeComments(Resource):
  @staticmethod
  def post():
    return process_add_recipe_comments(request)

# Get all brief info of the recipes that belongs to the current user
@recipe_namespace.route("/getMyRecipes")
class GetMyRecipes(Resource):
  @staticmethod
  def get():
    return process_get_my_recipes(request)

# Get all brief info of the recipes that tried by the current user
@recipe_namespace.route("/getMyTriedRecipes")
class GetMyTriedRecipes(Resource):
  @staticmethod
  def get():
    return process_get_my_tried_recipes(request)

# Get all brief info of recommended recipes
@recipe_namespace.route("/getRecommendedRecipes/<recipe_id>")
class GetRecommendedRecipes(Resource):
  @staticmethod
  def get(recipe_id):
    return process_get_recomended_recipes(recipe_id)

# Try a recipe
@recipe_namespace.route("/tryRecipe")
class TryRecipe(Resource):
  @staticmethod
  def put():
    return process_try_recipes(request)
