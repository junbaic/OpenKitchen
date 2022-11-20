import NavBar from './components/NavBar';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/homepage';
import Register from './pages/register';
import Login from './pages/login';
import Recipe from './pages/recipe';
import RecipeDetail from "./pages/recipe/detail";
import Setting from './pages/setting';
import Profile from './pages/profile';
import Search from './pages/search';
import { Layout } from 'antd';
import {LoginStateContextProvider} from './pages/LoginStateContext';
import {ModalVisibleStateContextProvider} from './pages/ModalVisibleStateContext';
import {IsUpdateContextProvider} from './pages/IsUpdateContext';
const { Footer } = Layout;

function App() {
  return (
    <div className="App">
      <div className="page-container">
        <LoginStateContextProvider>
          <IsUpdateContextProvider>
            <ModalVisibleStateContextProvider>
              <NavBar />
              <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/register" element={<Register />} />
                <Route path="/login" element={<Login />} />
                <Route path="/recipe" element={<Recipe />} />
                <Route path="/recipe/edit/:recipeId" element={<Recipe />} />
                <Route path="/recipe/:recipeId" element={<RecipeDetail />} />
                <Route path="/search/:keywords" element={<Search />} />
                <Route path="/profile/setting" element={<Setting />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/setting" element={<Setting />} />
              </Routes>
              <Footer style={{ backgroundColor: "#fff" }}>
                copyright @Team Sunflower
              </Footer>
            </ModalVisibleStateContextProvider>
          </IsUpdateContextProvider>
        </LoginStateContextProvider>
      </div>
    </div>
  );
}

export default App;