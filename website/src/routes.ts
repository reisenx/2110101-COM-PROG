import { index, route, type RouteConfig } from "@react-router/dev/routes";

export default [
  index("./routes/home.tsx"),
  route("search", "./routes/search.tsx"),
  route("404", "./routes/not-found.tsx"),
  route("*", "./routes/content.tsx"),
] satisfies RouteConfig;
