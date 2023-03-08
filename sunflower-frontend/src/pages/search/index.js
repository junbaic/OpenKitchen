import React, { useEffect, useState } from 'react';
import RecipeTab from '../homepage/RecipeTab';
import '../homepage/HomePage.css';
import { useParams } from "react-router-dom";

const axios = require('axios').default;
const HomePage = () => {
    const [allRecipes, setAllRecipes] = useState([]);
    const params = useParams();

    useEffect(() => {
        const searchUrl = 'http://127.0.0.1:8000/recipe/searchRecipe/'+params.keywords;

        const getRecipes = async () => {
            try {
                const { data } = await axios.get(searchUrl);
                const { recipe_briefInfo } = data;
                const recipes = recipe_briefInfo.map(recipe => ({ id: recipe['recipe_id'], recipeName: recipe['name'], photo: recipe['picture'], authorName: recipe['contributor'], like: recipe['like'] }));
                setAllRecipes(recipes);
            } catch (err) {
                return err;
            }
        }
        getRecipes();
    }, []);
    
    return (
        <main className="HomePage">
            <RecipeTab title={'All Searched Recipes'} columns={2} recipesArray={allRecipes}></RecipeTab>
        </main>
    )
};

export default HomePage;