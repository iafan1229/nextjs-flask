"use client";
import { useEffect } from "react";

export default function GetContentPage() {
  const getContent = async () => {
    try {
      const response = await fetch("http://localhost:3000/api/getContent", {
        // API URL을 Flask 서버에 맞게 조정
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      return data; // Returning the data to use in the useEffect
    } catch (error) {
      console.error("Error:", error);
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      const data = await getContent();
      console.log(data);
    };
    fetchData();
  }, []);

  return (
    <p>
      인스타그램 로그인에 성공하여 데이터 분석에 사용할 콘텐츠를 가져오는
      중입니다...
    </p>
  );
}
