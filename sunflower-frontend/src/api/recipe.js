import request from "../utils/request";

/**
 * @abstract: add recipe
 * @method addRecipe
 * @example:"recipe_id": 2,
 *
*/
export function addRecipe(data) {
  return request({
    url: "/recipe/createRecipe",
    method: "post",
    data,
  });
}

/**
 * @abstract: update recipe
 * @method updateRecipe
 * @example:"recipe_id": 2,
 *
*/
export function updateRecipe(data) {
  return request({
    url: "/recipe/updateRecipe",
    method: "put",
    data,
  });
}

/**
 * @abstract: delete a recipe
 * @method deleteRecipe
 * @example:"recipe_id": 2,
 *
*/
export function deleteRecipe(recipe_id) {
  return request({
    url: `/recipe/deleteRecipe/${recipe_id}`,
    method: "put",
  });
}

/**
 * @abstract: Get all detail info of a recipe
 * @method getRecipeById
 * @example:"recipe_id": 2,
 *
*/
export function getRecipeById(recipe_id) {
  return request({
    url: `/recipe/getRecipeDetailInfo/${recipe_id}`,
    method: "get",
  });
}


/**
 * @abstract Rating for a recipe
 * @method ratingByRecipeId
 * @example:{
    "recipe_id": 2,
    "rating": 1.5 
    }
 *
*/ 
export function ratingByRecipeId(data) {
  return request({
    url: "/recipe/ratingRecipe",
    method: "post",
    data,
  });
}


/**
 * @abstract  Get rating of a recipe
 * @method getRatingByRecipeId
 * @example:"recipe_id": 2,
 * 
  */ 
export function getRatingByRecipeId(recipe_id) {
  return request({
    url: `/recipe/getRecipeAverageRating/${recipe_id}`,
    method: "get",
  });
}

/**
 * @abstract  get comments by recipe id
 * @method getCommentByRecipeId
 * @example:"recipe_id": 2,
 * 
  */ 
export function getCommentByRecipeId(recipe_id) {
  return request({
    url: `/recipe/getRecipeComment/${recipe_id}`,
    method: "get",
  });
}


/**
 * @abstract  get comments by recipe id
 * @method getCommentByRecipeId
 * @example:{
    "recipe_id": 2, 
    "comment_content": "I like this recipe!" 
    }
 * 
*/ 
export function addCommentByRecipeId(data) {
  return request({
    url: "/recipe/addRecipeComments",
    method: "post",
    data,
  });
}


/**
 * @abstract  get user recipes
 * @method getMyRecipe
 * @example:null
 * 
 * * */

export function getMyRecipe() {
  return request({
    url: '/recipe/getMyRecipes',
    method: 'get',
  });
}

export function getRecommendedRecipesById(recipe_id) {
  return request({
    url: `/recipe/getRecommendedRecipes/${recipe_id}`,
    method: 'get',
  });
}

export function toggleTriedRecipes(data) {
  return request({
    url: `/recipe/tryRecipe`,
    method: 'put',
    data,
  })
}