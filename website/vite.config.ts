import { reactRouter } from "@react-router/dev/vite";
import { defineConfig } from "vite";

const configuredBasePath = process.env.SITE_BASE_PATH?.replace(/^\/+|\/+$/g, "");

export default defineConfig({
  base: configuredBasePath ? `/${configuredBasePath}/` : "/",
  plugins: [reactRouter()],
  publicDir: ".generated/public",
  resolve: {
    alias: {
      "~": new URL("./src", import.meta.url).pathname,
    },
  },
  build: {
    assetsInlineLimit: 2048,
  },
});
