import React, { useState } from "react";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui";
import { Button, Input, Label } from "@/components/ui";
import { Brain, RefreshCw, BarChart2, Save } from "lucide-react";

const ModelTraining = ({ dataset, onTrain }) => {
  const [targetColumn, setTargetColumn] = useState("");
  const [featureColumns, setFeatureColumns] = useState([]);
  const [modelType, setModelType] = useState("linear");
  const [learningRate, setLearningRate] = useState(0.01);
  const [maxDepth, setMaxDepth] = useState(5);
  const [epochs, setEpochs] = useState(50);
  const [isTraining, setIsTraining] = useState(false);
  const [metrics, setMetrics] = useState(null);

  if (!dataset || dataset.data.length === 0) {
    return (
      <div className="p-6 text-gray-500 dark:text-gray-300">
        No dataset selected. Please upload and select a dataset for training.
      </div>
    );
  }

  const handleFeatureSelection = (col) => {
    setFeatureColumns((prev) =>
      prev.includes(col) ? prev.filter((c) => c !== col) : [...prev, col]
    );
  };

  const trainModel = async () => {
    if (!targetColumn || featureColumns.length === 0) {
      alert("Please select a target column and at least one feature column.");
      return;
    }

    setIsTraining(true);
    // Simulating API request
    setTimeout(() => {
      const fakeMetrics = {
        accuracy: (Math.random() * 0.2 + 0.8).toFixed(2),
        r2: (Math.random() * 0.1 + 0.85).toFixed(2),
        mse: (Math.random() * 100 + 50).toFixed(2),
      };
      setMetrics(fakeMetrics);
      setIsTraining(false);
    }, 3000);
  };

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <h3 className="text-xl font-semibold mb-4">Train Machine Learning Model</h3>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="target-column">Target Column</Label>
          <Select value={targetColumn} onValueChange={setTargetColumn}>
            <SelectTrigger id="target-column">
              <SelectValue placeholder="Select target column" />
            </SelectTrigger>
            <SelectContent>
              {dataset.columns
                .filter((col) => !featureColumns.includes(col))
                .map((col) => (
                  <SelectItem key={col} value={col}>
                    {col}
                  </SelectItem>
                ))}
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-2">
          <Label htmlFor="model-type">Model Type</Label>
          <Select value={modelType} onValueChange={setModelType}>
            <SelectTrigger id="model-type">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="linear">Linear Regression</SelectItem>
              <SelectItem value="decision-tree">Decision Tree</SelectItem>
              <SelectItem value="random-forest">Random Forest</SelectItem>
              <SelectItem value="neural-network">Neural Network</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>

      <div className="mt-4 space-y-2">
        <Label>Select Feature Columns</Label>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
          {dataset.columns
            .filter((col) => col !== targetColumn)
            .map((col) => (
              <div key={col} className="flex items-center space-x-2">
                <input
                  type="checkbox"
                  id={`feature-${col}`}
                  checked={featureColumns.includes(col)}
                  onChange={() => handleFeatureSelection(col)}
                />
                <Label htmlFor={`feature-${col}`}>{col}</Label>
              </div>
            ))}
        </div>
      </div>

      {/* Hyperparameter Inputs */}
      <div className="grid grid-cols-3 gap-4 mt-4">
        <div className="space-y-2">
          <Label>Learning Rate</Label>
          <Input type="number" step="0.01" value={learningRate} onChange={(e) => setLearningRate(e.target.value)} />
        </div>
        <div className="space-y-2">
          <Label>Max Depth</Label>
          <Input type="number" value={maxDepth} onChange={(e) => setMaxDepth(e.target.value)} />
        </div>
        <div className="space-y-2">
          <Label>Epochs</Label>
          <Input type="number" value={epochs} onChange={(e) => setEpochs(e.target.value)} />
        </div>
      </div>

      <Button onClick={trainModel} disabled={isTraining} className="w-full mt-4">
        {isTraining ? (
          <>
            <RefreshCw className="mr-2 h-4 w-4 animate-spin" />
            Training...
          </>
        ) : (
          <>
            <Brain className="mr-2 h-4 w-4" />
            Train Model
          </>
        )}
      </Button>

      {metrics && (
        <div className="mt-6 p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">
          <h4 className="text-lg font-semibold mb-2">Model Performance</h4>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="border p-4 rounded text-center">
              <p className="text-sm text-gray-500">Accuracy</p>
              <p className="text-2xl font-bold">{(metrics.accuracy * 100).toFixed(1)}%</p>
            </div>
            <div className="border p-4 rounded text-center">
              <p className="text-sm text-gray-500">R² Score</p>
              <p className="text-2xl font-bold">{metrics.r2}</p>
            </div>
            <div className="border p-4 rounded text-center">
              <p className="text-sm text-gray-500">MSE</p>
              <p className="text-2xl font-bold">{metrics.mse}</p>
            </div>
          </div>
        </div>
      )}

      <div className="flex gap-4 mt-6">
        <Button variant="outline">
          <Save className="mr-2 h-4 w-4" />
          Save Model
        </Button>
        <Button variant="outline">
          <BarChart2 className="mr-2 h-4 w-4" />
          View Analysis
        </Button>
      </div>
    </div>
  );
};

export default ModelTraining;
