import React from "react";
import { Link } from "react-router-dom";
import Insights from "@/components/Insights";
import Charts from "@/components/Charts";
import { BarChart2, Brain, FileText } from "lucide-react";

const Dashboard = ({ dataset, insights, anomalies }) => {
  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <h2 className="text-2xl font-bold mb-6">Dashboard Overview</h2>

      {/* Insights Section */}
      <Insights insights={insights} anomalies={anomalies} />

      {/* Quick Navigation */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
        <Link to="/analysis" className="p-4 bg-blue-500 text-white rounded-lg flex items-center">
          <BarChart2 className="mr-2" /> Go to Analysis
        </Link>
        <Link to="/model-training" className="p-4 bg-green-500 text-white rounded-lg flex items-center">
          <Brain className="mr-2" /> Train a Model
        </Link>
        <Link to="/reports" className="p-4 bg-purple-500 text-white rounded-lg flex items-center">
          <FileText className="mr-2" /> View Reports
        </Link>
      </div>

      {/* Charts Section */}
      <div className="mt-6">
        <h3 className="text-xl font-semibold mb-4">Data Visualization</h3>
        <Charts dataset={dataset} />
      </div>
    </div>
  );
};

export default Dashboard;
