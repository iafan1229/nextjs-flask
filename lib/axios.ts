import axios from "axios";

export const instance = axios.create({
  baseURL: "http://127.0.0.1:8080",
  timeout: 100000, // 30초로 타임아웃 연장
});
