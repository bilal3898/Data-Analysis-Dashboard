import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@/context/AuthContext";
import { DatasetProvider } from "@/context/DatasetContext";
import { ThemeProvider, useTheme } from "@/context/ThemeContext";
import Sidebar from "@/components/Sidebar";
import Header from "@/components/Header";
import Dashboard from "@/pages/Dashboard";
import Analysis from "@/pages/Analysis";
import ModelTraining from "@/pages/ModelTraining";
import Reports from "@/pages/Reports";
import Settings from "@/pages/Settings";
import "./styles/global.css";

const Layout = ({ children }) => {
  const { darkMode } = useTheme();
  
  return (
    <div className={`flex h-screen ${darkMode ? "dark" : ""}`}>
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Header />
        <main className="p-6 overflow-auto">{children}</main>
      </div>
    </div>
  );
};

const App = () => {
  return (
    <ThemeProvider>
      <AuthProvider>
        <DatasetProvider>
          <Router>
            <Routes>
              <Route path="/" element={<Layout><Dashboard /></Layout>} />
              <Route path="/analysis" element={<Layout><Analysis /></Layout>} />
              <Route path="/model-training" element={<Layout><ModelTraining /></Layout>} />
              <Route path="/reports" element={<Layout><Reports /></Layout>} />
              <Route path="/settings" element={<Layout><Settings /></Layout>} />
            </Routes>
          </Router>
        </DatasetProvider>
      </AuthProvider>
    </ThemeProvider>
  );
};

export default App;
