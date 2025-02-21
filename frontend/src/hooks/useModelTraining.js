import { useState } from "react";
import { trainModel, getModelMetrics } from "@/api/mlApi";

const useModelTraining = () => {
  const [training, setTraining] = useState(false);
  const [modelMetrics, setModelMetrics] = useState(null);
  const [error, setError] = useState(null);

  const handleTrainModel = async (datasetId, targetColumn, featureColumns, modelType) => {
    setTraining(true);
    setError(null);

    try {
      const result = await trainModel(datasetId, targetColumn, featureColumns, modelType);
      setModelMetrics(result.metrics);
    } catch (err) {
      setError(err.message || "Model training failed");
    }

    setTraining(false);
  };

  const fetchModelMetrics = async (modelId) => {
    try {
      const metrics = await getModelMetrics(modelId);
      setModelMetrics(metrics);
    } catch (err) {
      setError(err.message || "Failed to fetch model metrics");
    }
  };

  return { handleTrainModel, fetchModelMetrics, modelMetrics, training, error };
};

export default useModelTraining;
