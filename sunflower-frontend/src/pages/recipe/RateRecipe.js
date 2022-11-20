import { Button, Modal, Rate, message } from 'antd';
import React, { useState } from 'react';
import './RateRecipe.css'

const RateRecipe = ({rate, recipe, changeState, isChange}) => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const desc = ['Terrible', 'Bad', 'Normal', 'Good', 'Wonderful!'];
    const [value, setValue] = useState(0);
    const showModal = () => {
        setIsModalOpen(true);
    };
    const handleOk = () => {
        setIsModalOpen(false);
    };
    const handleCancel = () => {
        setIsModalOpen(false);
    };

    const handleRate = async() => {
        const data = {
            recipe_id: recipe,
            rating: value
        }
        try{
            const res = await rate(data);
            message.success('Happy to receive your feedback!');
            changeState(!isChange);
            handleCancel();
        }catch(e){
            message.error('Sorry, rate fail');
            return e;
        }
    }

    return (
        <>
            <Button type="text" onClick={showModal} style={{color: 'black'}}>
                Rate
            </Button>
            <Modal open={isModalOpen} onOk={handleOk} onCancel={handleCancel} footer={null}>
                <div className="modal-container">
                    <h3 className='rate-modal--title'>Have you tried it? Rate it!</h3>
                    <p className='rate-modal--para'>What'd you think?</p>
                    <Rate tooltips={desc} onChange={setValue} value={value}/>
                    {value ? <span className="ant-rate-text">{desc[value - 1]}</span> : ''}
                    <button type='submit' className="rate-button" onClick={handleRate}>Rate</button>
                </div>
            </Modal>
        </>
    )
}

export default RateRecipe;