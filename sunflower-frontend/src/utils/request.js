import axios from "axios";
// import { getLoginStatus } from "@/utils/auth";
import { message } from "antd";

// Create Instance
const service = axios.create({
  // api_url
  //baseURL: 'http://127.0.0.1:8000',
  baseURL: 'http://ec2-52-194-185-52.ap-northeast-1.compute.amazonaws.com:8000',
  // request timeout
  timeout: 10 * 60 * 1000, 
});

const tokenHeader = "Authorization";

// Add request interceptor
service.interceptors.request.use(
  (config) => {
    // What to do before sending the request
    const token =
      localStorage.getItem("token") ||
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJEeWxhbiIsImV4cGlyeSI6IjIwMjItMTAtMTAgMDI6Mjg6NTQuMTkyODE5In0.p37txTY_PXO9JxDKjoaoMdFGyQYAZni5ZA6asOfd6Kc";
    if (token) {
      /* eslint-disable no-param-reassign */
      config.headers[tokenHeader] = token;
    }
    return config;
  },
  (reason) => {
    // What to do with request errors
    Promise.reject(reason);
  }
);

// Add Response Interceptor
service.interceptors.response.use(
  (res) => {
    // 2xx All status codes in the range trigger the function.
    // do something with range trigger
    // if (!getLoginStatus() && router.currentRoute.name !== "login") {
    //   store.dispatch("UserLogout").then(() => {
    //     router.push({ name: "login" });
    //   });
    // }
    return res;
  },
  (err) => {
    // The function will be triggered if the status code exceeds the range of 2xx.
    // Do something about response errors
    // console.log(err);
    // If an error occurs, judge whether it is 401 or 504
    if (err.response.status === 401 || err.response.status === 504) {
        message.warning("You are Not the Auth");
    } else {
      if (err.response.data || err.response) {
        message.info(err.response.data || err.response);
      } else {
        message.error("Service Error,Please wait the service");
      }
      return Promise.reject(err.response);
    }
    return Promise.reject(err.response);
  }
);

export default service;
