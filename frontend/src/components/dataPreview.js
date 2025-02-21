import React from "react";

const DataPreview = ({ dataset }) => {
  if (!dataset || dataset.data.length === 0) {
    return (
      <div className="p-4 text-gray-500 dark:text-gray-300">
        No dataset selected. Upload and select a dataset to preview.
      </div>
    );
  }

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <h3 className="text-xl font-semibold mb-4">{dataset.name} - Preview</h3>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300">
              {dataset.columns.map((col, index) => (
                <th key={index} className="p-2 border text-left">{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {dataset.data.slice(0, 5).map((row, rowIndex) => (
              <tr key={rowIndex} className="border-b hover:bg-gray-50 dark:hover:bg-gray-800">
                {dataset.columns.map((col, colIndex) => (
                  <td key={colIndex} className="p-2 border text-gray-800 dark:text-gray-300">
                    {row[col] !== undefined ? row[col] : "N/A"}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
        Showing first 5 rows of {dataset.data.length} total records.
      </p>
    </div>
  );
};

export default DataPreview;
