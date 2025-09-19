import React from "react";
import { Link } from "react-router-dom";

const Header: React.FC = () => {
  const logout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "/login";
  };
  const isAuth = Boolean(localStorage.getItem("access"));
  return (
    <header style={{ padding: 12, borderBottom: "1px solid #ddd" }}>
      <nav>
        <Link to="/">Home</Link> | <Link to="/school">School</Link> | <Link to="/profile">Profile</Link>
        {isAuth ? <button onClick={logout} style={{ marginLeft: 12 }}>Logout</button> : <Link to="/login" style={{ marginLeft: 12 }}>Login</Link>}
      </nav>
    </header>
  );
};
export default Header;
import React from 'react';

const Header: React.FC = () => {
    return (
        <header>
            <h1>School Site</h1>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/profile">Profile</a></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;