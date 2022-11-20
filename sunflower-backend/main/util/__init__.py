from datetime import datetime, timedelta
import jwt 
from flask import current_app
import nltk
from nltk import word_tokenize, pos_tag
nltk.download("wordnet", quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('omw-1.4', quiet=True)
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from ..table.mytable import *
# generate token
# reference: https://blog.csdn.net/weixin_58959719/article/details/125263952
def generate_token(user_name):
    # period of validity: 24h
    expiry = str(datetime.utcnow() + timedelta(hours=24))
    payload = {"user_name": user_name, "expiry": expiry}
    secret = current_app.config["SECRET_KEY"]
    # generate token  jwt.encode
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

# Verify token
def decode_token(token):
    secret = current_app.config["SECRET_KEY"]

    try:
        # verify token jwt.decode
        payload = jwt.decode(token, secret, algorithms="HS256")
    except Exception as e:
        print("error>>", e)
        # verity failed
        payload = None
    return payload


def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def get_recommended_recipes_id(rq_recipe_id, ingredient_table):
    rq_recipe_id = int(rq_recipe_id)
    rq_recipe_ingredients = ingredient_table.query.filter(ingredient_table.id_recipe == rq_recipe_id).all()
    other_recipes_id = []
    recommended_recipes_id = []
    for each in Recipe.query.all():
        if each.id != int(rq_recipe_id):
            other_recipes_id.append(each.id)

    for id in other_recipes_id:
        compare_recipe_ingredients = ingredient_table.query.filter(ingredient_table.id_recipe == id).all()
        intersect_ingredients = []
        union_ingredients = []
        for ingredient1 in rq_recipe_ingredients:
            ingredients_NONU_1 = []
            tokens1 = word_tokenize(ingredient1.ingredient_name)
            tagged_sent1 = pos_tag(tokens1)
            wnl = WordNetLemmatizer()
            for tag in tagged_sent1:
                wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
                # Only keep Noun
                if tag[1].startswith('N'):
                    ingredients_NONU_1.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # Lemmatization

            for ingredient2 in compare_recipe_ingredients:
                ingredients_NONU_2 = []
                tokens2 = word_tokenize(ingredient2.ingredient_name)
                tagged_sent2 = pos_tag(tokens2)
                wnl = WordNetLemmatizer()
                for tag in tagged_sent2:
                    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
                    # Only keep Noun
                    if tag[1].startswith('N'):
                        ingredients_NONU_2.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # Lemmatization

                if len(set(ingredients_NONU_1) & set(ingredients_NONU_2)) > 0:
                    for each in (set(ingredients_NONU_1) & set(ingredients_NONU_2)):
                        if each not in intersect_ingredients:
                            intersect_ingredients.append(each)
                for each in (set(ingredients_NONU_1) | set(ingredients_NONU_2)):
                    if each not in union_ingredients:
                        union_ingredients.append(each)

        # Calculate Jaccard similarity
        if (len(intersect_ingredients) / len(union_ingredients)) > 0.1:
            recommended_recipes_id.append((id, len(intersect_ingredients) / len(union_ingredients)))
    return recommended_recipes_id
