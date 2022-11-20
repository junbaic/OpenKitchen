import React, { useState, useEffect } from "react";
import "./index.css";
import {
  Row,
  Col,
  Button,
  Input, 
  message,
  Avatar
} from 'antd';
import { editSetting, GetUserInfo } from '../../api/editSetting';
import UploadFile from "./uploadFile";

const Setting = () => {
  const avatar = localStorage.getItem("avatar");
  const userName = localStorage.getItem("username");
  const bio = localStorage.getItem("bio");
  const email = localStorage.getItem("email");
  /* init components */
  const [userInfo, setUserInfo] = useState({
    username: userName,
    email: email,
    avatar: avatar,
    BIO: bio,
    password: "",
  });

  useEffect(() => {
    function getUserInfo() {
      GetUserInfo().then(
        (res) => {
          const pwd = res.data.password;
          setUserInfo({
            ...userInfo,
            password: pwd,
          });
        },
        (err) => {
          message.error("Get user information Failed!");
          return err;
        }
      );
    }
    getUserInfo();
  },[])

  function onNameChange(name) {
    setUserInfo({
      ...userInfo,
      username: name,
    });
  }

  function onPasswordChange(pwd) {
    setUserInfo({
      ...userInfo,
      password: pwd,
    });
  }

  function onEmailChange(email) {
    setUserInfo({
      ...userInfo,
      email: email,
    });
  }

  function onBioChange(bio) {
    setUserInfo({
      ...userInfo,
      BIO: bio,
    });
  }

  function handleFiles(photo) {
    setUserInfo({
      ...userInfo,
      avatar:photo.base64,
    });
  }

  async function onSubmit () {
    const data = {
      ...userInfo,
    };
    try {
      const res = await editSetting(data);
      message.success("Update Profile Success!");
      window.localStorage.bio = userInfo.BIO;
      window.localStorage.avatar = userInfo.avatar;
      window.localStorage.email = userInfo.email;
      setTimeout(() => {
        window.location.href='/profile/';
      }, 1000);
    } catch (error) {
      const status = error.status;
        if (status === 400){
          message.error("Username cannot be changed");
        }else{
          message.error("Update Profile Failed!");
        }
      return error;
    }
  }

  function onLogout() {
    message.success("Logout Success!");
    localStorage.clear();
    setTimeout(() => {
      window.location.href="/";
    }, 1000); 
}


  return (
    <main className="userInfo-container">
      <Row>
        <Col span={4}></Col>
        <Col span={16} className="userInfo-content-container">
          <p className="title-name">Edit Profile</p>
          <section className="info-section">
          <div className="info-row">
            <span className="info-title">AVATAR</span>
          </div>
          <div className='edit--avatar-container'>
                {
                    avatar ?
                        <Avatar shape="square" src={avatar} size={14} style={
                            {
                                borderRadius: '0.75rem',
                                backgroundColor: '#ffcd02',
                                height: '6.5rem',
                                width: '6.5rem',
                                display: 'block'
                            }}></Avatar>
                        :
                        <Avatar shape="square" size={14} style={{
                            color: '#fff',
                            backgroundColor: '#ffcd02',
                            borderRadius: '0.75rem',
                            display: 'block',
                            fontFamily: 'Lyon Text Web Semibold', 
                            fontSize: '4rem',
                            padding: '7%'
                        }}>{userName[0]}</Avatar>
                }
            </div>
            <div className="info-row">
              <UploadFile onFileChange={handleFiles}></UploadFile>
            </div>
            <div className="info-row">
              <h3 className="info-title">USERNAME</h3>
            </div>
            <div className="info-row">
              <Input
                placeholder="Please enter your username"
                value={userInfo.username}
                className="info-row-input"
                onChange={(e) => {
                  onNameChange(e.target.value);
                }}
              />
            </div>
            <div className="info-row">
              <h3 className="info-title">EMAIL</h3>
            </div>
            <div className="info-row">
              <Input
                placeholder="Please enter your email"
                value={userInfo.email}
                className="info-row-input"
                onChange={(e) => {
                  onEmailChange(e.target.value);
                }}
              />
            </div>
            <div className="info-row">
              <h3 className="info-title">BIO</h3>
            </div>
            <div className="info-row">
              <Input
                placeholder="Please enter your bio"
                value={userInfo.BIO}
                className="info-row-input"
                onChange={(e) => {
                  onBioChange(e.target.value);
                }}
              />
            </div>
          </section>
          <p className="title-name">Modify Password</p>
          <section className="info-section">
            <div className="info-row">
              <h3 className="info-title">PASSWORD</h3>
            </div>
            <div className="info-row">
              <Input
                placeholder="Please enter your password"
                value={userInfo.password}
                className="info-row-input"
                type='password'
                onChange={(e) => {
                  onPasswordChange(e.target.value);
                }}
              />
            </div>
          </section>
          <div className="info-btn">
            <Button type="primary" onClick={onSubmit}>
              Update Profile
            </Button>
          </div>
          <div className="info-btn">
            <Button type="primary" onClick={onLogout}>
              Logout
            </Button>
          </div>
        </Col>
        <Col span={4}></Col>
      </Row>
    </main>
  );
};

export default Setting;