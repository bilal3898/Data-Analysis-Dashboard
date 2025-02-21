import React from "react";
import { Settings, Moon, Sun } from "lucide-react";

const Header = ({ darkMode, setDarkMode }) => {
  return (
    <header className="flex justify-between items-center px-6 py-4 bg-white dark:bg-gray-900 shadow-md">
      <h1 className="text-2xl font-bold text-gray-800 dark:text-white">AI Analytics Dashboard</h1>
      
      <div className="flex items-center space-x-4">
        <button onClick={() => setDarkMode(!darkMode)} className="p-2 rounded-full bg-gray-100 dark:bg-gray-700">
          {darkMode ? <Sun className="text-yellow-500" /> : <Moon className="text-gray-600" />}
        </button>
        <button className="p-2 rounded-full bg-gray-100 dark:bg-gray-700">
          <Settings className="text-gray-600 dark:text-gray-300" />
        </button>
      </div>
    </header>
  );
};

export default Header;
