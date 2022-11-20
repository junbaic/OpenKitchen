import { Menu } from 'antd';
import { BookOutlined } from '@ant-design/icons';
import { GiRiceCooker } from "react-icons/gi";
import './ProfileNav.css';
import ProfileRecipes from '../profileRecipes';
import ProfileTried from '../profileTried';
import {useState} from 'react';

const ProfileNav = () => {
    const [tab, setTab] = useState('recipes');
    const nav_style= {
        display: 'flex', justifyContent: 'center', alignItems: 'center'
    }
    return (
        <>
            <nav className="ProfileNav" style={{fontFamily: 'TT commons'}}>
                <Menu mode="horizontal" defaultSelectedKeys={['recipes']}>
                    <Menu.Item key="recipes" 
                    icon={<BookOutlined style={{fontSize: '20px'}} className='profile-nav--recipes-icon nav--icon'/>}
                    style={nav_style}
                    onClick={()=> setTab('recipes')}
                    >
                        <div className="nav--item-name">recipes</div>
                    </Menu.Item>
                    <Menu.Item key='tried' 
                    icon={<GiRiceCooker style={{fontSize: '24px'}} className='profile-nav--tried-icon nav--icon'/>}
                    style={nav_style}
                    onClick={()=> setTab('tried')}>
                        <div className="nav--item-name">tried</div>
                    </Menu.Item>
                </Menu>
            </nav>
            <div className="profile-Tab-content--container">
                {
                    (tab === 'recipes') && <ProfileRecipes/>
                }
                {
                    (tab === 'tried') && <ProfileTried/>
                }
            </div>
        </>
    )
}

export default ProfileNav;