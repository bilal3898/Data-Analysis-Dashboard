import React, { useState } from "react";
import Charts from "@/components/Charts";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui";
import { Filter, BarChart2, LineChart, PieChart as PieChartIcon, ScatterPlot } from "lucide-react";

const Analysis = ({ dataset }) => {
  const [selectedMetric, setSelectedMetric] = useState("");

  if (!dataset || dataset.data.length === 0) {
    return (
      <div className="p-6 text-gray-500 dark:text-gray-300">
        No dataset selected. Please upload and select a dataset to analyze.
      </div>
    );
  }

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <h2 className="text-2xl font-bold mb-6">Data Analysis</h2>

      {/* Filter Options */}
      <div className="flex items-center gap-4 mb-6">
        <Filter className="text-gray-500" />
        <Select value={selectedMetric} onValueChange={setSelectedMetric}>
          <SelectTrigger className="w-60">
            <SelectValue placeholder="Select Metric" />
          </SelectTrigger>
          <SelectContent>
            {dataset.columns.map((col) => (
              <SelectItem key={col} value={col}>
                {col}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      {/* Charts */}
      <Charts dataset={dataset} />
    </div>
  );
};

export default Analysis;
