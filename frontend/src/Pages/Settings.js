import React, { useState } from "react";
import { Switch, Label, Input, Button } from "@/components/ui";
import { Settings, Sun, Moon, Key, RefreshCw } from "lucide-react";

const Settings = ({ darkMode, setDarkMode }) => {
  const [apiKey, setApiKey] = useState("************");
  const [language, setLanguage] = useState("en");
  const [notifications, setNotifications] = useState(true);

  const resetSettings = () => {
    setLanguage("en");
    setNotifications(true);
    alert("Dashboard settings have been reset!");
  };

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <h3 className="text-2xl font-bold mb-6 flex items-center">
        <Settings className="mr-2" />
        App Settings
      </h3>

      {/* Dark Mode Toggle */}
      <div className="flex items-center justify-between p-4 border rounded-lg mb-4">
        <div className="flex items-center">
          {darkMode ? <Moon className="text-gray-400 mr-2" /> : <Sun className="text-yellow-400 mr-2" />}
          <span>Dark Mode</span>
        </div>
        <Switch checked={darkMode} onCheckedChange={setDarkMode} />
      </div>

      {/* API Key Management */}
      <div className="p-4 border rounded-lg mb-4">
        <Label>API Key</Label>
        <div className="flex items-center gap-2 mt-2">
          <Input type="password" value={apiKey} readOnly className="w-full" />
          <Button variant="outline" onClick={() => setApiKey("NewAPIKey123456")}>
            <Key className="mr-2" />
            Generate New
          </Button>
        </div>
      </div>

      {/* User Preferences */}
      <div className="p-4 border rounded-lg mb-4">
        <h4 className="font-semibold mb-2">User Preferences</h4>

        <div className="mb-3">
          <Label>Language</Label>
          <select
            className="p-2 border rounded w-full"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="es">Spanish</option>
          </select>
        </div>

        <div className="flex items-center justify-between">
          <Label>Enable Notifications</Label>
          <Switch checked={notifications} onCheckedChange={setNotifications} />
        </div>
      </div>

      {/* Reset Settings */}
      <Button variant="destructive" className="w-full mt-4" onClick={resetSettings}>
        <RefreshCw className="mr-2" />
        Reset Dashboard Settings
      </Button>
    </div>
  );
};

export default Settings;
