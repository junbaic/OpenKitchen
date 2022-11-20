import React from 'react';
import './Login.css';
import { useNavigate } from 'react-router-dom';
import { useLoginStateContext } from '../../pages/LoginStateContext';
import axios from 'axios';
import Register from '../../pages/register';
import { useModalVisibleStateContext } from '../ModalVisibleStateContext';
import {
  Form,
  Input,
  message,
  Button,
  Modal
} from "antd";

export default function Login() {
  const { setIsLogged } = useLoginStateContext();

  const { isRegisterModalVisible, setIsRegisterModalVisible, setIsModalOpen } = useModalVisibleStateContext();
  const closeLoginModal = () => {
    setIsModalOpen(false);
  };

  const showRegisterModal = () => {
    setIsRegisterModalVisible(true);
    closeLoginModal();
  };

  const handleRegisterCancel = () => {
    setIsRegisterModalVisible(false);
  };

  const onFinish = values => {
    axios.post("http://ec2-52-194-185-52.ap-northeast-1.compute.amazonaws.com:8000/user/login", values)
      .then( res => {
        message.success('Welcome back!');
        window.localStorage.token = res.data.token;
        window.localStorage.username = res.data.username;
        window.localStorage.avatar = res.data.avatar;
        window.localStorage.email = res.data.email;
        window.localStorage.bio = res.data.BIO;
        setIsLogged(true);
        navigate('/');
      })
      .catch(err => {
        if (err.response.status === 400){
          message.error('Please input the correct name and password~');
        }
      })
  };

  const navigate = useNavigate();
  return (
    <div className="login">
      <img className='login--peace-hand__center' src='/peace_hand.svg' alt='peace_hand'></img>
      <h1 className='login-title'>Welcome Back</h1>
      <Form
        name="normal_login"
        className="login-form"
        layout='vertical'
        initialValues={{ remember: true }}
        onFinish={onFinish}
        style={{ rowGap: '0.5rem', width: '83.333333%', display: 'flex', flexDirection: 'column', alignItems: 'center'}}
      >
        <Form.Item
          label={<span className='loginForm-itemName'>Username</span>}
          name="username"
          rules={[{ required: true, message: 'Please input your Username!' }]}
          style={{width: '100%'}}
        >
          <Input
            style={{ borderRadius: '0.25rem', border: '1px solid #6b7280', padding: '0.5rem 0.75rem' }}
          />
        </Form.Item>
        <Form.Item
          label={<span className='loginForm-itemName'>Password</span>}
          name="password"
          rules={[{ required: true, message: 'Please input your Password!' }]}
          style={{width: '100%'}}
        >
          <Input
            type="password"
            style={{ borderRadius: '0.25rem', border: '1px solid #6b7280', padding: '0.5rem 0.75rem' }}
          />
        </Form.Item>

        <Form.Item style={{margin: 0}}>
          <button type='submit' className="login-form-button">Log in</button>
        </Form.Item>
        <Form.Item>
          <Button onClick={showRegisterModal} style={{margin: '0', border: 'none', fontFamily: 'TT commons'}}>I don’t have an account Sign-up!</Button>
          <Modal open={isRegisterModalVisible} footer={null} onCancel={handleRegisterCancel} >
            <Register />
          </Modal>
        </Form.Item>
      </Form>
    </div>


  );
}