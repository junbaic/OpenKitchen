import { createContext, useContext, useState } from 'react';

const ModalVisibleStateContext = createContext(
    {
        isRegisterModalVisible: false,
        setIsRegisterModalVisible: undefined,
        isModalOpen: false,
        setIsModalOpen: undefined
    });


export const ModalVisibleStateContextProvider = ({ children }) => {
    const [isRegisterModalVisible, setIsRegisterModalVisible] = useState(false);
    const [isModalOpen, setIsModalOpen] = useState(false);

    return (
        <ModalVisibleStateContext.Provider value={
            {
                isRegisterModalVisible,
                setIsRegisterModalVisible,
                isModalOpen,
                setIsModalOpen
            }}>
            {children}</ModalVisibleStateContext.Provider>
    )
};


export const useModalVisibleStateContext = () => useContext(ModalVisibleStateContext);