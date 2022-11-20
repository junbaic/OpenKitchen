import './ProfileRecipes.css';
import NoRecipesPage from './noRecipesPage';
import ProfileRecipeCard from './profileRecipeCard';
import {Link} from 'react-router-dom';
import {useState, useEffect} from 'react';

const axios = require('axios').default;

const ProfileRecipes = () => {
    const accessToken = localStorage.getItem("token");

    const [allRecipes, setAllRecipes] = useState([]);
    const config = {
        headers: { Authorization: `${accessToken}` }
    };
    const fetchRecipes = async () => {
      try{
        const { data } = await axios.get('http://ec2-52-194-185-52.ap-northeast-1.compute.amazonaws.com:8000/recipe/getMyRecipes', config);
        const { my_recipes } = data;
        const recipesList = my_recipes.map((recipe) => ({ id: recipe['recipe_id'], recipeName: recipe['name'], photo: recipe['picture'], authorName: recipe['contributor'], mealType: recipe['meal_type'], like: recipe['like'], following: 'yes'}));
        setAllRecipes(recipesList);
      }catch(e){
        console.log(e);
      }
    };
    useEffect(() => {
        fetchRecipes();
    },[])
    return (
      <div className="profile-recipes--grid-container">
        {
        allRecipes.length > 0 
        ? 
        (
          <ul className="recipes-grid">
            {allRecipes.map(({ id, ...rest }) => (
              <ProfileRecipeCard key={id} recipeId={id} {...rest}
              callbackAfterDelete={fetchRecipes}
              />
            ))}
            <button className="create-new-recipe-button">
              <Link to='/recipe'>
                <div className='button-content'>
                  <img className="button-icon" src='/addNewRecipe.svg' alt='addNewRecipe'></img>
                  <span className='button-text'>
                    Create a new recipe
                    </span>
                </div>
              </Link>
            </button>

          </ul>
        ) : (
          <NoRecipesPage />
        )}
      </div>
    );
}

export default ProfileRecipes;