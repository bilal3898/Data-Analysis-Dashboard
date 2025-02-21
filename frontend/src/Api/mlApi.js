import apiClient from "./apiClient";

const ML_ENDPOINT = "/ml";

// Train ML Model
export const trainModel = async (datasetId, targetColumn, featureColumns, modelType) => {
  try {
    const response = await apiClient.post(`${ML_ENDPOINT}/train`, {
      dataset_id: datasetId,
      target_column: targetColumn,
      feature_columns: featureColumns,
      model_type: modelType,
    });

    return response.data;
  } catch (error) {
    throw error;
  }
};

// Get Model Metrics
export const getModelMetrics = async (modelId) => {
  try {
    const response = await apiClient.get(`${ML_ENDPOINT}/metrics/${modelId}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Make Predictions
export const makePrediction = async (modelId, inputData) => {
  try {
    const response = await apiClient.post(`${ML_ENDPOINT}/predict`, {
      model_id: modelId,
      input_data: inputData,
    });

    return response.data;
  } catch (error) {
    throw error;
  }
};
