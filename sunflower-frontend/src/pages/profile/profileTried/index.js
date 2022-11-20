import ProfileTriedCard from "../../../components/profileTriedCard";
import NoRecipesPage from './noRecipesPage';
import './ProfileTried.css';
import { useState, useEffect } from 'react';

const axios = require('axios').default;

const ProfileTried = () => {
  const accessToken = localStorage.getItem("token");

  const [allRecipes, setAllRecipes] = useState([]);
  const config = {
    headers: { Authorization: `${accessToken}` }
  };

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const { data } = await axios.get('http://ec2-52-194-185-52.ap-northeast-1.compute.amazonaws.com:8000/recipe/getMyTriedRecipes', config);
        const { my_recipes } = data;
        const recipesList = my_recipes.map(recipe => ({ id: recipe['recipe_id'], recipeName: recipe['name'], photo: recipe['picture'], authorName: recipe['contributor'], like: recipe['like'], following: 'yes' }));
        setAllRecipes(recipesList);
      } catch (e) {
        return e;
      }
    };
    fetchRecipes();
  }, [])

  return (
    <div className="profile-recipes--grid-container">
      {
        allRecipes.length > 0
          ?
          <ul className="tried-recipes-grid">
            {allRecipes.map(({ id, authorName, recipeName, photo, like, following }) =>
              <ProfileTriedCard key={id} recipeId={id} author={authorName} title={recipeName} picture={photo} like={like} following={following} />
            )}
          </ul>
          :
          <NoRecipesPage />
      }
    </div>
  )
}

export default ProfileTried;