"use client";

import { useEffect } from "react";

export default function Home() {
  useEffect(() => {
    // 클라이언트 측에서 API 호출
    async function openBrowser() {
      try {
        let response = await fetch("http://localhost:3000/api/open-browser");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const result = await response.text();
        console.log(result);
      } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
      }
    }

    openBrowser(); // 페이지 로드 시 API 호출
  }, []);

  return <div>브라우저 열기 시도 중...</div>;
}
