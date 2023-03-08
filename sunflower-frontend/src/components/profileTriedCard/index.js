import {useState, useEffect} from 'react';
import axios from 'axios';
import {message} from 'antd';
import {HeartOutlined, PlusOutlined, HeartFilled, MinusOutlined} from '@ant-design/icons';
import './ProfileTriedCard.css';
import {useIsUpdateContext} from '../../pages/IsUpdateContext';
import {Link} from 'react-router-dom';


const ProfileTriedCard = ({recipeId, author, title, picture, like, following}) => {
    const accessToken = localStorage.getItem("token");
    const [isLike, setIsLike] = useState(like === 'yes'? true: false);
    const [isFollow, setIsFollow] = useState(following === 'yes'? true: false);
    const {isUpdate, setIsUpdate} = useIsUpdateContext();
    const config = {
                    headers: { Authorization: `${accessToken}` }
                };

    const toggleLikeRequest = async () => {
        const {data} = await axios.put('http://127.0.0.1:8000/recipe/likeRecipe', {recipe_id: recipeId},config);
        setIsLike(!isLike);
        setIsUpdate(!isUpdate);
        message.success(data.msg);
    }
    const toggleFollowRequest = async () => {
        const {data} = await axios.put('http://127.0.0.1:8000/user/followingUser', {recipe_id: recipeId},config);
        setIsFollow(!isFollow);
        setIsUpdate(!isUpdate);
        message.success(data.msg);
    }
    useEffect(() => {
        setIsLike(like === 'yes'? true: false);
        setIsFollow(following === 'yes'? true: false);
    },[like, following])
    
    return (
        <li className="recipe-card-container">
            <Link to={`/recipe/${recipeId}`}>
                <div className='photo-container'>
                    <img className="recipe-photo" src={picture} alt="recipe"/>
                </div>
            </Link>
                <div className="recipe-name-container">
                    <Link to={`/recipe/${recipeId}`}>
                        <h3 className="recipe-name">{title}</h3>
                    </Link>
                    <div className="RecipeCard--like-container">
                    {
                        accessToken ? 
                        isLike 
                        ?<HeartFilled style={{color: 'red'}} onClick={toggleLikeRequest}/>
                        :<HeartOutlined style={{color: 'red'}} onClick={toggleLikeRequest}/>
                        :
                        <HeartOutlined style={{color: 'red'}}/>
                    }
                    </div>
                </div>
            
            <div className="RecipeCard--author-name">
                <span className="recipe-author">{author}</span>
                {
                    accessToken ? 
                    isFollow
                    ?<MinusOutlined style={{fontSize:'15px'}} onClick={toggleFollowRequest}/>
                    :<PlusOutlined style={{fontSize:'15px'}} onClick={toggleFollowRequest}/>
                    :
                    <PlusOutlined style={{fontSize:'15px'}}/>
                }
            </div>
        </li>        
    )
};

export default ProfileTriedCard;