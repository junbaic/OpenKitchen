import './noRecipesPage.css';
import {Link} from 'react-router-dom';

const NoRecipesPage = () => {
    return (
        <div className="empty-state">
            <img className='empty-state--img' src='/recipe-empty-state.png' alt='empty state' />
            <h3 className="empty-state--title">
                Want to publish your own recipes on OpenKitchen?
            </h3>
            <p className="empty-state--paragraph">
                Now's the time! Click below to upload your recipe to share with the community!
            </p>
            <Link to='/recipe'><button className='empty-state--button'>
                Share your first recipe
            </button></Link>
        </div>
    )
}

export default NoRecipesPage;