import request from "../utils/request";

export function editSetting(data) {
  return request({
    url: "/user/modifyProfile",
    method: "put",
    data,
  });
}

export function GetUserInfo() {
  return request({
    url: "/user/getUesrInfo",
    method: "get",
  });
}
