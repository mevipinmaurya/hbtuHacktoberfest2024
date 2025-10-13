import React from 'react';
import { Routes, Route } from "react-router-dom";
import NotFound from "./pages/NotFound";
import FunFact from "./components/FunFact";

function App() {
  return (
    <Routes>
      {/* 👇 Home route */}
      <Route
        path="/"
        element={
          <div style={{ textAlign: "center", marginTop: "2rem" }}>
            <h1>Welcome to HBTU Hacktoberfest!</h1>
            <FunFact />
          </div>
        }
      />

      {/* 👇 Catch-all route */}
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default App;

