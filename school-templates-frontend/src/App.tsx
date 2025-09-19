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
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './templates/Header/Header';
import Footer from './templates/Footer/Footer';
import Layout from './templates/Layout/Layout';
import Home from './pages/Home';
import About from './pages/About';
import SchoolHome from './templates/School/SchoolHome';
import SchoolProfile from './templates/School/SchoolProfile';

const App: React.FC = () => {
  return (
    <Router>
      <Layout>
        <Header />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" component={About} />
          <Route path="/school" exact component={SchoolHome} />
          <Route path="/school/profile" component={SchoolProfile} />
        </Switch>
        <Footer />
      </Layout>
    </Router>
  );
};

export default App;