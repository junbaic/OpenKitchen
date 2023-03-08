import React, { useEffect, useState } from 'react';
import RecipeTab from './RecipeTab';
import './HomePage.css';
import {useLoginStateContext} from '../../pages/LoginStateContext';
import {useIsUpdateContext} from '../../pages/IsUpdateContext';

const axios = require('axios').default;

const HomePage = () => {
    const [allRecipes, setAllRecipes] = useState([]);
    const [followingRecipes, setFollowingRecipes] = useState([]);
    const {isUpdate} = useIsUpdateContext();
    const accessToken = localStorage.getItem("token");
    const {isLogged} = useLoginStateContext();
    const config = {
                    headers: { Authorization: `${accessToken}` }
                };
    useEffect(() => {
        
        const getAllRecipes = async () => {
            try {
                const { data } = 
                isLogged
                ?
                await axios.get('http://127.0.0.1:8000/recipe/getAllRecipesBriefInfo', config)
                : 
                await axios.get('http://127.0.0.1:8000/recipe/getAllRecipesBriefInfo')
                const { recipe_briefInfo } = data;
                const recipes = recipe_briefInfo.map(recipe => ({ id: recipe['recipe_id'], recipeName: recipe['name'], photo: recipe['picture'], authorName: recipe['contributor'], like: recipe['like'], following: recipe['following'] }));
                setAllRecipes(recipes);
            } catch (err) {
                return err;
            }
        }
        getAllRecipes();
    }, [isLogged, isUpdate]);


    useEffect(() => {
        const getFollowingRecipes = async () => {
            try {
                const { data } = await axios.get('http://127.0.0.1:8000/recipe/getFollowingRecipe', config);
                const { recipe_briefInfo } = data;
                const recipes = recipe_briefInfo.map(recipe => ({ id: recipe['recipe_id'], recipeName: recipe['name'], photo: recipe['picture'], authorName: recipe['contributor'], like: recipe['like'], following: recipe['following']  }));
                setFollowingRecipes(recipes);
            } catch (err) {
                return err;
            }
        }
        getFollowingRecipes();
    }, [isLogged, isUpdate]);
    
    return (
        <main className="HomePage">
            <RecipeTab title={'All Recipes'} columns={2} recipesArray={allRecipes}></RecipeTab>
            <RecipeTab title={'Following Recipes'} columns={2} recipesArray={followingRecipes}></RecipeTab>
        </main>
    )
};

export default HomePage;