import {createContext, useContext, useState} from 'react';

const accessToken = localStorage.getItem("token");
const LoginStateContext = createContext({isLogged: Boolean(accessToken), setIsLogged: undefined});

export const LoginStateContextProvider = ({children}) => {
    
    const [isLogged, setIsLogged] = useState(Boolean(accessToken));
    return (
        <LoginStateContext.Provider value={{isLogged, setIsLogged}}>{children}</LoginStateContext.Provider>
    )
};
    

export const useLoginStateContext = () => useContext(LoginStateContext);