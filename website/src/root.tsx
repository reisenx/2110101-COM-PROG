import type { ReactNode } from "react";
import {
  isRouteErrorResponse,
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "react-router";

import { SITE } from "./config/site";
import "./styles/theme.css";
import "./styles/global.css";

export function Layout({ children }: { children: ReactNode }) {
  return (
    <html lang="th">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="#ffffff" />
        <Meta />
        <Links />
      </head>
      <body>
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App() {
  return <Outlet />;
}

export function ErrorBoundary({ error }: { error: unknown }) {
  const message = isRouteErrorResponse(error)
    ? `${error.status} ${error.statusText}`
    : error instanceof Error
      ? error.message
      : "เกิดข้อผิดพลาดที่ไม่คาดคิด";

  return (
    <main className="fatal-error" id="main-content">
      <div className="brand-mark" aria-hidden="true">
        <span>&lt;/</span>
        <span>&gt;</span>
      </div>
      <p>{SITE.name}</p>
      <h1>ไม่สามารถเปิดหน้านี้ได้</h1>
      <p>{message}</p>
      <a href={SITE.basePath}>กลับหน้าแรก</a>
    </main>
  );
}
