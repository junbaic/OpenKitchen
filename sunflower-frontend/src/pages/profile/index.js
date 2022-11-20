import './profile.css';
import ProfileHeader from './profileHeader';
import ProfileNav from './profileNav';

const Profile = () => {
    return (
        <main className='profile--main__pt'>
            <section>
                <ProfileHeader />
            </section>
            <ProfileNav/>
        </main>
    )
};

export default Profile;