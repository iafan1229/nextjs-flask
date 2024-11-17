"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import GetContentPage from "../app/getContent/page";
import Login from "./login";

export default function Pages() {
  const router = useRouter();
  const [userId, setUserId] = useState(undefined);

  return (
    <>
      <Login userId={userId ?? undefined} setUserId={setUserId} />
      {userId ? (
        <GetContentPage userId={userId ?? undefined} setUserId={setUserId} />
      ) : null}
      {/* {!userId ? (
        <Login userId={userId ?? undefined} setUserId={setUserId} />
      ) : (
        <GetContentPage userId={userId ?? undefined} setUserId={setUserId} />
      )} */}
    </>
  );
}
