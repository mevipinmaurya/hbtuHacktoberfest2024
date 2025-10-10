// src/pages/NotFound.jsx
import React from "react";
import { useNavigate } from "react-router-dom";

const NotFound = () => {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 text-center px-4">
      <h1 className="text-6xl font-bold text-red-500 mb-4 animate-bounce">404</h1>
      <h2 className="text-2xl font-semibold mb-2">Page Not Found 😢</h2>
      <p className="text-gray-600 mb-6 max-w-md">
        Oops! The page you are looking for does not exist. Maybe try going back home or check the URL.
      </p>
      <button
        onClick={() => navigate("/")}
        className="px-6 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transform hover:scale-105 transition duration-300"
      >
        Go Home
      </button>
    </div>
  );
};

export default NotFound;
