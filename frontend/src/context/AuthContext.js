import React, { createContext, useContext, useState, useEffect } from "react";
import apiClient from "@/api/apiClient";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("authToken") || null);

  useEffect(() => {
    if (token) {
      localStorage.setItem("authToken", token);
      fetchUser();
    } else {
      localStorage.removeItem("authToken");
      setUser(null);
    }
  }, [token]);

  const fetchUser = async () => {
    try {
      const response = await apiClient.get("/auth/me");
      setUser(response.data);
    } catch (error) {
      console.error("Error fetching user:", error);
      logout();
    }
  };

  const login = async (email, password) => {
    try {
      const response = await apiClient.post("/auth/login", { email, password });
      setToken(response.data.token);
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  const logout = () => {
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
