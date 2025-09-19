import React, { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

const Register: React.FC = () => {
  const [form, setForm] = useState({ username: "", password: "", email: "" });
  const nav = useNavigate();
  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.register(form);
      nav("/login");
    } catch {
      alert("Register failed");
    }
  };
  return (
    <form onSubmit={submit}>
      <h2>Register</h2>
      <input placeholder="username" value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })} />
      <input placeholder="email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
      <input placeholder="password" type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} />
      <button type="submit">Register</button>
    </form>
  );
};
export default Register;
