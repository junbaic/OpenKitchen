import { Avatar } from 'antd';
import Icon, { SettingOutlined } from '@ant-design/icons';
import './ProfileHeader.css';

const ProfileHeader = () => {
    const avatar = localStorage.getItem("avatar");
    const userName = localStorage.getItem("username");
    const bio = localStorage.getItem("bio");
    return (
        <section className='profile--header'>
            <section className='profile--header-setting'>
                <a href='/profile/setting' className='profile--setting-link'>
                    <Icon component={SettingOutlined} className='setting-icon' />
                    <span className='Setting-link--text'>Settings</span>
                </a>
            </section>
            <div className='profile--avatar-container'>
                {
                    avatar ?
                        <Avatar shape="square" src={avatar} style={
                            {
                                borderRadius: '0.75rem',
                                backgroundColor: '#ffcd02',
                                height: '11rem',
                                width: '11rem',
                                display: 'block'
                            }}></Avatar>
                        :
                        <Avatar shape="square"  style={{
                            color: '#fff',
                            backgroundColor: '#ffcd02',
                            borderRadius: '0.75rem',
                            height: '11rem',
                            width: '11rem',
                            display: 'block',
                            fontFamily: 'Lyon Text Web Semibold', 
                            fontSize: '8rem',
                            padding: '40%'
                        }}>{userName[0]}</Avatar>
                }
            </div>
            <section className='profile--header-info_alignLeft'>
                <div className='header--user-info'>
                    <h2 className='header--user-info__name'>{userName}</h2>
                </div>
                <div className='header--user-bio'>
                    <p className='header--user-bio__text'>{bio}</p>
                </div>
            </section>
        </section>
    )
}

export default ProfileHeader;