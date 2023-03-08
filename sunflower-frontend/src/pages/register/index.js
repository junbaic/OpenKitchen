import React from 'react';
import { useLoginStateContext } from '../../pages/LoginStateContext';
import Login from '../login';
import './Register.css';
import { useNavigate } from 'react-router-dom';
import { useModalVisibleStateContext } from '../ModalVisibleStateContext';

import axios from 'axios'
import {
  Form,
  Input,
  Button,
  Modal,
  message
} from "antd";


export default function Register() {
  const { setIsLogged } = useLoginStateContext();
  const { isModalOpen, setIsModalOpen, setIsRegisterModalVisible } = useModalVisibleStateContext();
  const closeRegisterModal = () => {
    setIsRegisterModalVisible(false);
  }
  const showModal = () => {
    setIsModalOpen(true);
    closeRegisterModal();
  };
  const handleCancel = () => {
    setIsModalOpen(false);
  };
  const [form] = Form.useForm();
  const time = new Date().toJSON().slice(0, 19).replace("T", " "); //time 1
  const handleSubmit = values => {
    axios.post("http://127.0.0.1:8000/user/register", values)
      .then(function (response) {
        message.success('Welcome to OpenKitchen');
        window.localStorage.token = response.data.token;
        window.localStorage.username = response.data.username;
        setIsLogged(true);
        navigate('/');
      })
      .catch(err => err)
  };

  const navigate = useNavigate();
  return (
    <div className="register">
      <img className='register--wave-hand__center' src='/wave_hand.svg' alt='wave_hand' />
      <h1 className='register-title'>Welcome to OpenKitchen!</h1>
      <p className='register-paragraph__start'>Create your account</p>
      <Form
        form={form}
        name="register"
        onFinish={handleSubmit}
        layout='vertical'
        initialValues={{
          create_time: time,
        }}
        scrollToFirstError
        style={{ rowGap: '0.5rem', width: '83.333333%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}
      >

        <Form.Item
          label={<span className='registerForm-itemName'>email</span>}
          name="email"
          style={{ width: '100%' }}
          rules={[
            {
              required: true,
              message: "Email cannot be empty.",
            },
            {
              type: "email",
              message: "Invalid email.",
            },
          ]}
        >
          <Input style={{ borderRadius: '0.25rem', border: '1px solid #6b7280', padding: '0.5rem 0.75rem' }} />
        </Form.Item>
        <Form.Item
          label={<span className='registerForm-itemName'>username</span>}
          name="username"
          tooltip="Please enter your username~"
          style={{ width: '100%' }}
          rules={[
            {
              required: true,
              message: "Username cannot be empty.",
              whitespace: true, 
            },
          ]}
        >
          <Input style={{ borderRadius: '0.25rem', border: '1px solid #6b7280', padding: '0.5rem 0.75rem' }} />
        </Form.Item>
        <Form.Item
          hasFeedback
          label={<span className='registerForm-itemName'>password</span>}
          name="password"
          style={{ width: '100%' }}
          rules={[
            {
              required: true,
              message: "Password cannot be empty.",
            },
          ]}
        >
          <Input.Password style={{ borderRadius: '0.25rem', border: '1px solid #6b7280', padding: '0.5rem 0.75rem' }} />
        </Form.Item>
        <Form.Item
          hasFeedback
          label={<span className='registerForm-itemName'>confirm password</span>}
          name="confirmPassword"
          style={{ width: '100%' }}
          dependencies={["password"]} 
          rules={[
            {
              required: true,
              message: "Please confirm your password.",
            },
            (props) => {
              return {
                validator(_, value) {
                  if (!value || props.getFieldValue("password") === value) {
                    return Promise.resolve();
                  } else {
                    return Promise.reject(new Error("Password mismatch"));
                  }
                },
              };
            },
          ]}
        >
          <Input.Password style={{ borderRadius: '0.25rem', border: '1px solid #6b7280', padding: '0.5rem 0.75rem' }} />
        </Form.Item>
        <Form.Item style={{margin: 0}}>
          <button type='submit' className="register-form-button">Submit</button>
        </Form.Item>
        <Form.Item>
          <Button type='default' onClick={showModal} style={{margin: '0', border: 'none', fontFamily:'TT commons'}}>I already have an account.</Button>
          <Modal open={isModalOpen} footer={null} onCancel={handleCancel}>
            <Login />
          </Modal>
        </Form.Item>
      </Form>
    </div>
  );
}