const path = require("path");
/** @type {import('next').NextConfig} */
const nextConfig = {
  sassOptions: {
    includePaths: [path.join(__dirname, "styles")],
  },
  // rewrites: async () => {
  //   return [
  //     {
  //       source: "/api/:path*",
  //       destination:
  //         process.env.NODE_ENV === "development"
  //           ? "http://127.0.0.1:8080/api/:path*"
  //           : "/api/",
  //     },
  //   ];
  // },
  async rewrites() {
    return [
      {
        source: "/api/v1/:path*/",
        destination: `https://openapi.naver.com/v1/:path*/`,
      },
    ];
  },
};

module.exports = nextConfig;
