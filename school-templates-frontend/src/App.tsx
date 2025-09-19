import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Layout from "./templates/Layout/Layout";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Profile from "./templates/School/SchoolProfile";
import SchoolHome from "./templates/School/SchoolHome";

function App() {
  const isAuthenticated = Boolean(localStorage.getItem("access"));
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/school" element={isAuthenticated ? <SchoolHome /> : <Navigate to="/login" />} />
        <Route path="/profile" element={isAuthenticated ? <Profile /> : <Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Layout>
  );
}

export default App;