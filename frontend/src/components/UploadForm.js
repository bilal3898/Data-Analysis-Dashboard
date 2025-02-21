import React, { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { Upload, Trash2, FileSpreadsheet, AlertCircle } from "lucide-react";

const UploadForm = ({ onUpload }) => {
  const [files, setFiles] = useState([]);
  const [error, setError] = useState(null);

  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    if (rejectedFiles.length > 0) {
      setError("Invalid file format or size exceeded (Max 100MB).");
      return;
    }

    setFiles([...files, ...acceptedFiles]);
    setError(null);
  }, [files]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "text/csv": [".csv"],
      "application/json": [".json"],
      "application/vnd.ms-excel": [".xls"],
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [".xlsx"]
    },
    maxSize: 100 * 1024 * 1024, // 100MB
    multiple: true
  });

  const handleRemoveFile = (fileName) => {
    setFiles(files.filter(file => file.name !== fileName));
  };

  const handleUpload = () => {
    if (files.length === 0) {
      setError("No files selected for upload.");
      return;
    }

    onUpload(files);
    setFiles([]);
  };

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <h3 className="text-xl font-semibold mb-4">Upload Your Data</h3>

      <div
        {...getRootProps()}
        className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer ${
          isDragActive ? "border-blue-500 bg-blue-50" : "border-gray-300 dark:border-gray-600"
        }`}
      >
        <input {...getInputProps()} />
        <Upload className="mx-auto h-12 w-12 text-gray-400" />
        <p className="mt-2 text-gray-700 dark:text-gray-300">
          {isDragActive ? "Drop files here" : "Drag & drop files here or click to select"}
        </p>
        <p className="text-sm text-gray-500 mt-1">Supports CSV, JSON, XLSX (Max: 100MB)</p>
      </div>

      {error && (
        <div className="mt-4 flex items-center bg-red-100 text-red-600 p-3 rounded-lg">
          <AlertCircle className="mr-2" /> {error}
        </div>
      )}

      {files.length > 0 && (
        <div className="mt-4">
          <h4 className="font-semibold mb-2">Selected Files:</h4>
          <ul className="space-y-2">
            {files.map((file, index) => (
              <li key={index} className="flex items-center justify-between p-3 bg-gray-100 dark:bg-gray-800 rounded-lg">
                <div className="flex items-center space-x-2">
                  <FileSpreadsheet className="text-blue-500" />
                  <span>{file.name}</span>
                </div>
                <button onClick={() => handleRemoveFile(file.name)} className="text-red-500 hover:text-red-700">
                  <Trash2 />
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}

      <button
        onClick={handleUpload}
        className="mt-4 w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg"
      >
        Upload Files
      </button>
    </div>
  );
};

export default UploadForm;
