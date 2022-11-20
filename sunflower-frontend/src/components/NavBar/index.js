import { Input, Avatar, Button, Modal, Tooltip } from 'antd';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Link } from 'react-router-dom';
import React from 'react';
import "./NavBar.css";
import { useLoginStateContext } from '../../pages/LoginStateContext';
import { useModalVisibleStateContext } from '../../pages/ModalVisibleStateContext';
import Login from '../../pages/login';

const TTCommon = {fontFamily: 'TT commons'};
const { Search } = Input;

const onSearch = (value) => {
    const searchUrl = '/search/'+value;
    window.location.href=searchUrl
}

const NavBar = () => {
    const userName = localStorage.getItem("username");
    const avatar = localStorage.getItem("avatar");
    const { isLogged } = useLoginStateContext();
    const { isModalOpen,setIsModalOpen } = useModalVisibleStateContext();
    const showModal = () => {
        setIsModalOpen(true);
    };
    const handleCancel = () => {
        setIsModalOpen(false);
    };

    return (
        <div className="NavBar-container">
            <div className="NavBar--logo">
                <Link to='/' style={{color: '#000'}}><span >OpenKitchen</span></Link>
            </div>
            <div className="NavBar--search-input">
    
                <Search 
                    size="large" 
                    placeholder="What would you like to cook?" 
                    suffix={
                        <Tooltip title="ingredient:<keywords>&method:<keywords>&mealType:<keywords>&recipeName:<keywords>">
                            <InfoCircleOutlined
                                style={{
                                color: 'rgba(0,0,0,.45)',
                                }}
                            />
                        </Tooltip>
                    }
                    style={TTCommon} 
                    onSearch={onSearch} 
                />
            </div>
            <div className="NavBar--avatar">
                {
                    isLogged
                        ?
                        <Link to='/profile'><Avatar shape="square" src={avatar} style={{ fontSize: '17.28px', color: '#fff', backgroundColor: '#ffcd02', borderRadius: '5px' }}>{userName[0]}</Avatar></Link>
                        :
                        <>
                            <Button type="text" onClick={showModal} style={{fontSize: '1rem', lineHeight: '1.5rem', fontFamily:'TT commons', fontWeight:'560'}} >Sign-in</Button>
                            <Modal open={isModalOpen} footer={null} onCancel={handleCancel}>
                                <Login />
                            </Modal>
                        </>}
            </div>
        </div>
    )

}

export default NavBar;