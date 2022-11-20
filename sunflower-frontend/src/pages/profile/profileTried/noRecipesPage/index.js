import './NoRecipesPage.css';
import {Link} from 'react-router-dom';

const NoRecipesPage = () => {
    return (
        <div className="empty-state">
            <img className='empty-state--img' src='/recipe-empty-state.png' alt='empty state' />
            <h3 className="empty-state--title">
                You have no tried recipes now!
            </h3>
            <p className="empty-state--paragraph">
                Now's the time! Click below to find more interested recipes!
            </p>
            <Link to='/'><button className='empty-state--button'>
                Enjoy~
            </button></Link>
        </div>
    )
}

export default NoRecipesPage;