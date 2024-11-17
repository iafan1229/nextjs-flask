"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import Login from "./Login";
import GetContentPage from "../app/getContent/page";

export default function Pages() {
  const router = useRouter();
  const [userId, setUserId] = useState(undefined);

  return (
    <>
      {!userId ? (
        <Login userId={userId ?? undefined} setUserId={setUserId} />
      ) : (
        <GetContentPage userId={userId ?? undefined} setUserId={setUserId} />
      )}
    </>
  );
}
