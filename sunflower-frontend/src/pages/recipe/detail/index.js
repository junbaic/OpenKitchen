import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import "../index.css";
import {
  Row,
  Col,
  Button,
  Input,
  Breadcrumb,
  Avatar,
  Rate,
  message,
  Divider,
} from "antd";
import { HeartOutlined, HeartFilled } from "@ant-design/icons";
import {
  getRecipeById,
  ratingByRecipeId,
  getRatingByRecipeId,
  getCommentByRecipeId,
  addCommentByRecipeId,
  getRecommendedRecipesById,
  toggleTriedRecipes
} from "../../../api/recipe";
import ProfileTriedCard from "../../../components/profileTriedCard";
import RateRecipe from "../RateRecipe";

const { TextArea } = Input;
const RecipeDetail = (props) => {
  /* init components */
  const [recipe, setRecipe] = useState({
    recipe_name: "",
    recipe_picture: "",
    meal_type: "Breakfast",
    create_time: "",
    contributor: "",
  });
  const [isTried, setIsTried] = useState(false);
  const [rate, setRate] = useState(0);
  const [ingredients, setIngredients] = useState([]);
  const [methods, setMethods]  = useState([]);
  const [comments, setComments]  = useState([]);
  const [recommendedRecipes, setRecommendedRecipes] = useState([]);
  const [isUpdate, setIsUpdate] = useState(false);

  const params = useParams();
  const { recipeId } = params;

  let comment = '';

  const userName = localStorage.getItem("username");
  const avatar = localStorage.getItem("avatar");
  useEffect(() => {
    
    getRecipeById(recipeId).then((res) => {
        if(res.status === 200) {
          const data = res.data.data;
          setRecipe({
            recipe_name: data.recipe_name,
            recipe_picture: data.recipe_picture,
            meal_type: data.meal_type,
            create_time: data.create_time,
            contributor: data.contributor,
          });
          setIngredients(data.ingredients);
          setMethods(data.methods);
        }
    }, (err) => {
        message.error("Get Recipe Detail Failed!");
    })
    getRatingByRecipeId(recipeId).then(
      (res) => {
        if (res.status === 200) {
          const data = res.data;
          if (data.recipe_average_rating
            ) {
            setRate(Number(data.recipe_average_rating
              ));
          }
        }
      },
      (err) => {
        message.error("Get Recipe Rate Failed!");
      }
    );
    getCommentByRecipeId(recipeId).then(
      (res) => {
        if (res.status === 200) {
          const data = res.data;
          if(data.data) {
            setComments(data.data);
          } 
        }
      },
      (err) => {
        message.error("Get Recipe Comment Failed!");
      }
    );
    getRecommendedRecipesById(recipeId).then( (res) => {
      if (res.status === 200) {
        const data = res.data;
        if(data.my_recipes) {
          setRecommendedRecipes(data.my_recipes);
        } 
      }
    },
    (err) => {
      message.error("Get Recommended Recipe Failed!");
    }
  );
  }, [recipeId, isUpdate])

  /* data */
  const toggleLike = async () =>{
    try{
      const recipe = parseInt(recipeId);
      const data = {
        recipe_id: recipe
      }
      const res = await toggleTriedRecipes(data);
      setIsTried(!isTried);
      message.success(res.data.msg);
    }catch(e){
      message.error('Sorry, tried recipe fail');
      return e;
    }
  }

  function onCommentChange(e) {
    comment = e.target.value;
  }

  function onSubmit() {
    const data = {
      recipe_id: recipeId,
      comment_content: comment,
    };
    addCommentByRecipeId(data).then((res) => {
      if(res.status=== 200) {
        message.success("Add Comment Success!");
        getCommentByRecipeId(recipeId).then(
          (res) => {
            if (res.status=== 200) {
              if(res.data) {
                const data = res.data;
                setComments(data.data);
              }
              
            }
          },
          (err) => {
            message.error("Get Recipe Detail Failed!");
          }
        );
      }
    }, (err) => {
      message.error("Add Comment Failed!");
    });
  }

  function getTimeString(time) {
    // const timeStr = new Date(new Date(time).toUTCString()).getTime();
    const timeStr = new Date(time).getTime();
    const nowTimeStr = new Date().getTime();
    const num = nowTimeStr - timeStr;
    // day
    const dayDiff = Math.floor(num / (24*3600*1000))
    // hour
    const leave1 = num % (24 * 3600 * 1000);
    const hours = Math.floor(leave1/(3600*1000));
    // minute
    const leave2 = leave1 % (3600 * 1000);
    const minutes = Math.floor(leave2 / (60 * 1000));
    // second
    const leave3 = leave2 % (60 * 1000);
    const seconds = Math.floor(leave3 / 1000);
    let timeString = time;
    if(dayDiff > 30) {
      timeString = time;
    } else if(dayDiff > 0) {
      timeString = `${dayDiff} days ago`;
    } else if(hours > 0) {
      timeString = `${hours} hours ago`;
    } else if(minutes > 0) {
      timeString = `${minutes} minutes ago`;
    } else {
      timeString = `${seconds} seconds ago`;
    }
    return timeString;
  }

  return (
    <main>
      <Row>
        <Col span={4}></Col>
        <Col span={16} className="recipe-detail-container">
          <Breadcrumb className="recipe-content-breadcrumb">
            <Breadcrumb.Item>RECIPE</Breadcrumb.Item>
            <Breadcrumb.Item>FISH DISHES</Breadcrumb.Item>
            <Breadcrumb.Item>
              {recipe.recipe_name.toUpperCase()}
            </Breadcrumb.Item>
          </Breadcrumb>
          <section className="recipe-detail-content">
            <img
              className="recipe-detail-photo detail-items"
              src={recipe.recipe_picture}
              alt="recipe"
            />
            <Row className="detail-items inner-link">
              <Col span={6}>
                <span>NAVIGATION BAR:</span>
              </Col>
              <Col span={6}>
                <a href="#Ingredients">Ingredients</a>
              </Col>
              <Col span={6}>
                <a href="#Methods">Methods</a>
              </Col>
              <Col span={6}>
                <a href="#Comments">Comments</a>
              </Col>
            </Row>
            <div className="detail-items">
              <span style={{fontFamily:"Lyon Text Web Semibold"}}>Meal-Type:</span>
              <span className="detail-content">{recipe.meal_type}</span>
            </div>
            <Divider></Divider>
            <div className="detail-items">
              <div className="recipe-detail-name">
                <span
                  className="detail-name-content"
                  title={recipe.recipe_name}
                >
                  {recipe.recipe_name}
                </span>
                <Rate disabled value={rate}></Rate>
                {isTried ? (
                  <HeartFilled
                    style={{ color: "red" }}
                    className="detail-like"
                    onClick={toggleLike}
                  />
                ) : (
                  <HeartOutlined className="detail-like" onClick={toggleLike} />
                )}
                <RateRecipe rate={ratingByRecipeId} recipe={recipeId} changeState={setIsUpdate} isChange={isUpdate}> </RateRecipe>
              </div>
              <div className="recipe-detail-author">
                <Avatar size={60}>U</Avatar>
                <div className="recipe-detail-author-detail">
                  <span className="author-text">{recipe.contributor}</span>
                  <span className="author-text">Contributor</span>
                </div>
              </div>
            </div>
            <Divider></Divider>
            <h2 className="items-title">Ingredients</h2>
            <div className="detail-items" id="Ingredients">
              {ingredients.map((item, i) => (
                <div className="detail-ingredient" key={{ i }}>
                  <div className="detail-ingredient-num-container">
                    <span className="detail-ingredient-num">
                      {item.ingredient_num}
                    </span>
                    <span>{item.ingredient_unit}</span>
                  </div>
                  <div>
                    <span className="detail-ingredient-name">
                      {item.ingredient_name}
                    </span>
                  </div>
                </div>
              ))}
            </div>
            <Divider></Divider>
            <h2 className="items-title">Methods</h2>
            <div className="detail-items" id="Methods">
              {methods.map((item, i) => (
                <div key={{ i }} className="method-container">
                  <span className="method-content">
                    {item.method_step}.{item.method_content}
                  </span>
                  <div>
                    <img src={item.method_photo} className="method-content-img" alt="imgh" />
                  </div>
                </div>
              ))}
            </div>
            <Divider></Divider>
            <h2 className="items-title">Comments({comments.length})</h2>
            {avatar?(
            <div className="comment-edit-container">
              <Avatar
                src={avatar}
                style={{
                  fontSize: "17.28px",
                  color: "#fff",
                  backgroundColor: "#ffcd02",
                }}
              >
                {userName[0]}
              </Avatar>
              <div className="comment-input">
                <TextArea
                  showCount
                  style={{ height: 120, resize: "none" }}
                  placeholder="Your comment here..."
                  onChange={onCommentChange}
                ></TextArea>
                <Button onClick={onSubmit} className="comment-submit">
                  Send
                </Button>
              </div>
            </div>
            ):("")}
            {comments.length ? (
              <div className="detail-items" id="Comments">
                {comments.map((item, i) => (
                  <div key={{ i }}>
                    <div className="comment-edit-container">
                      <div>
                        <Avatar
                          style={{
                            fontSize: "17.28px",
                            color: "#fff",
                            backgroundColor: "#ffcd02",
                          }}
                        >
                          {item.comment_username[0].toUpperCase()}
                        </Avatar>
                      </div>
                      <div className="comment-user-content">
                        <p>{item.comment_username}</p>
                        <p>{getTimeString(item.comment_time)}</p>
                        <p>{item.content}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <p className="comment-content">
                There are no reactions yet, Be the first to share your cooking
                experience!
              </p>
            )}
            <Divider></Divider>
            <h2 className="items-title">More delicious ideas for you </h2>
            <div className="recipe-detail-recommend">
            {comments.length ? (
              <ul className="tried-recipes-grid">
              {recommendedRecipes.map(recipe => (
                <ProfileTriedCard key={recipe.recipe_id} recipeId = {recipe.recipe_id} 
                author={recipe.contributor} title={recipe.name} picture={recipe.picture}
                like={recipe.like} following={recipe.following}/>
              ))}
              </ul>):
              (
                <p className="comment-content">
                  There are no more recommend yet!
                </p>
              )}
            </div>
          </section>
        </Col>
        <Col span={4}></Col>
      </Row>
    </main>
  );
};

export default RecipeDetail;
