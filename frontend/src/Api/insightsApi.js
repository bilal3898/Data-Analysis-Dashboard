import apiClient from "./apiClient";

const INSIGHTS_ENDPOINT = "/insights";

// Fetch AI-Generated Insights
export const fetchInsights = async (datasetId) => {
  try {
    const response = await apiClient.get(`${INSIGHTS_ENDPOINT}/${datasetId}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Detect Anomalies in Data
export const detectAnomalies = async (datasetId) => {
  try {
    const response = await apiClient.get(`${INSIGHTS_ENDPOINT}/anomalies/${datasetId}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Generate Data Recommendations
export const generateRecommendations = async (datasetId) => {
  try {
    const response = await apiClient.get(`${INSIGHTS_ENDPOINT}/recommendations/${datasetId}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};
