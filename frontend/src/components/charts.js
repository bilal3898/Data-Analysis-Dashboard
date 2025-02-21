import React, { useState } from "react";
import {
  LineChart, BarChart, PieChart, ScatterChart,
  Line, Bar, Pie, Scatter, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer, Cell
} from "recharts";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui";
import { BarChart2, PieChart as PieChartIcon, ScatterPlot, LineChart as LineChartIcon } from "lucide-react";

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#AF19FF'];

const Charts = ({ dataset }) => {
  const [chartType, setChartType] = useState("line");

  if (!dataset || dataset.data.length === 0) {
    return (
      <div className="p-4 text-gray-500 dark:text-gray-300">
        No dataset selected. Upload and select a dataset to visualize.
      </div>
    );
  }

  const renderChart = () => {
    switch (chartType) {
      case "bar":
        return (
          <BarChart data={dataset.data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey={dataset.columns[0]} />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey={dataset.columns[1]} fill="#8884d8" />
          </BarChart>
        );

      case "pie":
        return (
          <PieChart>
            <Pie data={dataset.data} dataKey={dataset.columns[1]} nameKey={dataset.columns[0]} cx="50%" cy="50%" outerRadius={100}>
              {dataset.data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        );

      case "scatter":
        return (
          <ScatterChart margin={{ top: 20, right: 30, bottom: 5, left: 20 }}>
            <CartesianGrid />
            <XAxis type="number" dataKey={dataset.columns[1]} name={dataset.columns[1]} />
            <YAxis type="number" dataKey={dataset.columns[2]} name={dataset.columns[2]} />
            <Tooltip cursor={{ strokeDasharray: "3 3" }} />
            <Legend />
            <Scatter name="Data Points" data={dataset.data} fill="#8884d8" />
          </ScatterChart>
        );

      default:
        return (
          <LineChart data={dataset.data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey={dataset.columns[0]} />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey={dataset.columns[1]} stroke="#8884d8" />
          </LineChart>
        );
    }
  };

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-semibold">Data Visualization</h3>
        <Select value={chartType} onValueChange={setChartType}>
          <SelectTrigger className="w-36">
            <SelectValue placeholder="Chart Type" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="line"><LineChartIcon className="inline-block mr-2" /> Line Chart</SelectItem>
            <SelectItem value="bar"><BarChart2 className="inline-block mr-2" /> Bar Chart</SelectItem>
            <SelectItem value="pie"><PieChartIcon className="inline-block mr-2" /> Pie Chart</SelectItem>
            <SelectItem value="scatter"><ScatterPlot className="inline-block mr-2" /> Scatter Chart</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <div className="h-96">
        <ResponsiveContainer width="100%" height="100%">
          {renderChart()}
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default Charts;
