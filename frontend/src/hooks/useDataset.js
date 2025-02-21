import { useState, useEffect } from "react";
import { fetchDatasets, uploadDataset, deleteDataset } from "@/api/datasetApi";

const useDataset = () => {
  const [datasets, setDatasets] = useState([]);
  const [selectedDataset, setSelectedDataset] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadDatasets();
  }, []);

  const loadDatasets = async () => {
    setLoading(true);
    try {
      const data = await fetchDatasets();
      setDatasets(data);
      if (data.length > 0) setSelectedDataset(data[0]);
    } catch (error) {
      console.error("Error fetching datasets:", error);
    }
    setLoading(false);
  };

  const handleUpload = async (file) => {
    setLoading(true);
    try {
      const newDataset = await uploadDataset(file);
      setDatasets([...datasets, newDataset]);
      setSelectedDataset(newDataset);
    } catch (error) {
      console.error("Error uploading dataset:", error);
    }
    setLoading(false);
  };

  const handleDelete = async (datasetId) => {
    setLoading(true);
    try {
      await deleteDataset(datasetId);
      setDatasets(datasets.filter((d) => d.id !== datasetId));
      if (selectedDataset?.id === datasetId) setSelectedDataset(null);
    } catch (error) {
      console.error("Error deleting dataset:", error);
    }
    setLoading(false);
  };

  return { datasets, selectedDataset, setSelectedDataset, handleUpload, handleDelete, loading };
};

export default useDataset;
