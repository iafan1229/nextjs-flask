import "@/styles/globals.scss";

export default async function Home() {
  let data = await fetch("http://localhost:3000/api/python");
  const result = await data.text();
  console.log(result);
  return <div>dd</div>;
}
