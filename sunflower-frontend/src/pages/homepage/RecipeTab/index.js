import ProfileTriedCard from "../../../components/profileTriedCard";
import './RecipeTab.css';
import { Button } from 'antd';
import { useState } from 'react';

const RecipeTab = (props) => {
    const [showMore, setShowMore] = useState(false);
    const noRecipesShowing = <li className="NoRecipes">It has nothing here now~</li>;
    const numberOfShowing = showMore ? props.recipesArray.length : 6;

    return (
        <div className="RecipeTab-container">
            <div className="RecipeTab--title__alignLeft">
                <h2>{props.title}</h2>
            </div>
            <div className="RecipeTab-content">
                <ul className="Recipes-list">
                    {   
                        props.recipesArray.length > 0 ?
                            props.recipesArray.slice(0, numberOfShowing)?.map(({ id, authorName, recipeName, photo, like, following }) => 
                                <ProfileTriedCard key={id} recipeId = {id} author={authorName} title={recipeName} picture={photo} like={like} following={following}/>
                            )
                    : noRecipesShowing
                    }
                </ul>
                {
                    (props.recipesArray.length > 6 && !showMore) &&
                    <div className="RecipesTab--button__more">
                        <Button type="primary" onClick={() => setShowMore(true)} style={{
                            fontFamily: 'TT commons', 
                            backgroundColor: '#faf5f0', 
                            border: '1px solid #33319f',
                            borderRadius:'10px', 
                            fontWeight: '500',
                            letterSpacing: '.04em',
                            lineHeight: '1.2',
                            color: '#33319f',
                            fontSize: '105%',
                            padding: '-10px'}}>More</Button>
                    </div>
                }
            </div>
        </div>
    )
};

export default RecipeTab;