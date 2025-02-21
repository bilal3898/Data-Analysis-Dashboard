import React, { createContext, useContext, useState } from "react";
import useDataset from "@/hooks/useDataset";

const DatasetContext = createContext();

export const DatasetProvider = ({ children }) => {
  const { datasets, selectedDataset, setSelectedDataset, handleUpload, handleDelete, loading } = useDataset();
  
  return (
    <DatasetContext.Provider value={{ datasets, selectedDataset, setSelectedDataset, handleUpload, handleDelete, loading }}>
      {children}
    </DatasetContext.Provider>
  );
};

export const useDatasetContext = () => useContext(DatasetContext);
