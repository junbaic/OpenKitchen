import {createContext, useContext, useState} from 'react';

const IsUpdateContext = createContext({isUpdate: false, setIsUpdate: undefined});

export const IsUpdateContextProvider = ({children}) => {
    
    const [isUpdate, setIsUpdate] = useState(false);
    return (
        <IsUpdateContext.Provider value={{isUpdate, setIsUpdate}}>{children}</IsUpdateContext.Provider>
    )
};
    

export const useIsUpdateContext = () => useContext(IsUpdateContext);