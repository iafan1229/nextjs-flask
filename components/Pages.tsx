"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function Pages() {
  const router = useRouter();

  useEffect(() => {
    console.log(router);
    if (router) router.push("/login");
  }, [router]);
  return <></>;
}
