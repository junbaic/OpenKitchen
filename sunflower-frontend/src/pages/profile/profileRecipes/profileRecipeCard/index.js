import './ProfileRecipeCard.css';
import {Link} from 'react-router-dom';
import DropdownMenu from '../dropdownMenu';

const ProfileRecipeCard = ({recipeName, recipeId, photo, mealType, callbackAfterDelete}) => {
    return (
      <li className="recipe-card-container">
        <Link to={`/recipe/${recipeId}`}>
          <div className="photo-container">
            <img className='recipe-photo' src={photo} alt='recipe'></img>
          </div>
          <section className='recipe-meal-type'>
            <div className='recipe-meal-type-text'>{mealType}</div>
          </section>
          <h3 className='recipe-name' style={{display: 'inline'}}>{recipeName}</h3>
        </Link>
        <DropdownMenu
          recipeId={recipeId}
          callbackAfterDelete={callbackAfterDelete}
        ></DropdownMenu>
      </li>
    );
}

export default ProfileRecipeCard;