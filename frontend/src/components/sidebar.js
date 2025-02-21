import React, { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { LayoutDashboard, BarChart2, Brain, FileText, Settings, Menu } from "lucide-react";

const Sidebar = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const location = useLocation();

  const menuItems = [
    { name: "Dashboard", icon: <LayoutDashboard />, path: "/" },
    { name: "Analysis", icon: <BarChart2 />, path: "/analysis" },
    { name: "Model Training", icon: <Brain />, path: "/model-training" },
    { name: "Reports", icon: <FileText />, path: "/reports" },
    { name: "Settings", icon: <Settings />, path: "/settings" }
  ];

  return (
    <aside className={`h-screen bg-white dark:bg-gray-900 shadow-md transition-all ${isCollapsed ? "w-16" : "w-64"} p-4`}>
      <button
        onClick={() => setIsCollapsed(!isCollapsed)}
        className="mb-6 p-2 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700"
      >
        <Menu />
      </button>

      <nav className="space-y-2">
        {menuItems.map((item, index) => (
          <Link
            key={index}
            to={item.path}
            className={`flex items-center p-3 rounded-lg transition-colors ${
              location.pathname === item.path
                ? "bg-blue-500 text-white"
                : "text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800"
            }`}
          >
            <span className="mr-3">{item.icon}</span>
            {!isCollapsed && <span>{item.name}</span>}
          </Link>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
