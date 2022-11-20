from .. import db
from sqlalchemy.dialects.mysql import LONGTEXT
# Create User table, it is primary table
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # user_id
    username = db.Column(db.String(64), nullable=False, unique=True)  # A unique identifier
    password = db.Column(db.String(64), nullable=False)
    avatar = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(64), nullable=False)
    BIO = db.Column(db.Text, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)  # front-end -> back-end
    following = db.Column(db.Text, nullable=True)  # following users
    like = db.Column(db.Text, nullable=True)  # user like recip id
    tried = db.Column(db.Text, nullable=True)  # user tried recip id

    recipes = db.relationship('Recipe', backref='uesr')  # Associate with a recipe table


# Create Recipe table
class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)  # recipe_id
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'), nullable=False)
    name = db.Column(db.Text, nullable=False)
    picture = db.Column(LONGTEXT, nullable=False)
    meal_type = db.Column(db.Enum('Breakfast', 'Lunch', 'Dinner'), nullable=False)
    create_time = db.Column(db.DateTime(), nullable=False)

    ingredients = db.relationship('Recipe_Ingredient', backref='recipe')  # Associate with the ingredient table
    methods = db.relationship('Recipe_Method', backref='recipe')  # Associate with the method table
    comments = db.relationship('Recipe_Comment', backref='recipe')  # Associate with the comment table
    ratings = db.relationship('Recipe_Rating', backref='recipe')  # Associate with the rating table


# create Recipe_Ingredient table
class Recipe_Ingredient(db.Model):
    __tablename__ = "recipe_ingredient"
    id = db.Column(db.Integer, primary_key=True)
    id_recipe = db.Column(db.Integer, db.ForeignKey("recipe.id", ondelete='CASCADE'), nullable=False)  # recipe_id
    ingredient_name = db.Column(db.String(64), nullable=False)
    ingredient_num = db.Column(db.Integer, nullable=False)
    ingredient_unit = db.Column(db.String(64), nullable=False)


# create Recipe_Method table
class Recipe_Method(db.Model):
    __tablename__ = "recipe_method"
    id = db.Column(db.Integer, primary_key=True)
    id_recipe = db.Column(db.Integer, db.ForeignKey("recipe.id", ondelete='CASCADE'), nullable=False)  # recipe_id
    method_step = db.Column(db.Integer, nullable=False)
    method_content = db.Column(db.Text, nullable=False)
    method_photo = db.Column(LONGTEXT, nullable=False)
    method_photo_file_name = db.Column(db.Text, nullable=False)


# create Recipe_Comment table
class Recipe_Comment(db.Model):
    __tablename__ = "recipe_comment"
    id = db.Column(db.Integer, primary_key=True)
    id_recipe = db.Column(db.Integer, db.ForeignKey("recipe.id", ondelete='CASCADE'), nullable=False)
    comment_time = db.Column(db.DateTime(), nullable=False)
    comment_username = db.Column(db.String(32), nullable=False)
    comment_content = db.Column(db.Text, nullable=False)
    # comment_photo = db.Column(db.Text, nullable=True)


# create Recipe_Rating table
class Recipe_Rating(db.Model):
    __tablename__ = "recipe_rating"
    id = db.Column(db.Integer, primary_key=True)
    id_recipe = db.Column(db.Integer, db.ForeignKey("recipe.id", ondelete='CASCADE'), nullable=False)  # recipe_id
    rating_time = db.Column(db.DateTime(), nullable=False)  # rating time
    rating_username = db.Column(db.String(32), nullable=False)  # user name
    rating = db.Column(db.Text, nullable=False)  # rating scale