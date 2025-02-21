import { useState } from "react";
import { fetchInsights, detectAnomalies, generateRecommendations } from "@/api/insightsApi";

const useInsights = () => {
  const [insights, setInsights] = useState([]);
  const [anomalies, setAnomalies] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchAIInsights = async (datasetId) => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchInsights(datasetId);
      setInsights(data);
    } catch (err) {
      setError(err.message || "Failed to fetch insights");
    }
    setLoading(false);
  };

  const fetchAnomalies = async (datasetId) => {
    setLoading(true);
    setError(null);
    try {
      const data = await detectAnomalies(datasetId);
      setAnomalies(data);
    } catch (err) {
      setError(err.message || "Failed to detect anomalies");
    }
    setLoading(false);
  };

  const fetchRecommendations = async (datasetId) => {
    setLoading(true);
    setError(null);
    try {
      const data = await generateRecommendations(datasetId);
      setRecommendations(data);
    } catch (err) {
      setError(err.message || "Failed to fetch recommendations");
    }
    setLoading(false);
  };

  return {
    insights,
    anomalies,
    recommendations,
    fetchAIInsights,
    fetchAnomalies,
    fetchRecommendations,
    loading,
    error,
  };
};

export default useInsights;
