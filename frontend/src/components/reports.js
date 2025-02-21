import React, { useState } from "react";
import { Button } from "@/components/ui";
import { Download, FileText, Trash2, FileSpreadsheet } from "lucide-react";

const Reports = () => {
  const [reports, setReports] = useState([
    { id: 1, name: "Revenue_Predictions_Q1_2024.xlsx", date: "2024-02-10", size: "850 KB", format: "xlsx" },
    { id: 2, name: "Customer_Segments_Analysis.pdf", date: "2024-01-28", size: "2.1 MB", format: "pdf" },
  ]);

  const generateReport = (format) => {
    const reportName = `Generated_Report_${new Date().toISOString().split("T")[0]}.${format}`;
    const newReport = {
      id: reports.length + 1,
      name: reportName,
      date: new Date().toISOString().split("T")[0],
      size: "Unknown",
      format,
    };
    setReports([newReport, ...reports]);
  };

  const deleteReport = (id) => {
    setReports(reports.filter((report) => report.id !== id));
  };

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <h3 className="text-xl font-semibold mb-4">Generate & Download Reports</h3>

      {/* Report Generation Buttons */}
      <div className="flex gap-4">
        <Button variant="outline" onClick={() => generateReport("pdf")}>
          <FileText className="mr-2 h-4 w-4" />
          Generate PDF
        </Button>
        <Button variant="outline" onClick={() => generateReport("xlsx")}>
          <FileSpreadsheet className="mr-2 h-4 w-4" />
          Generate Excel
        </Button>
      </div>

      {/* List of Generated Reports */}
      <div className="mt-6">
        <h4 className="font-semibold mb-2">Available Reports</h4>
        {reports.length > 0 ? (
          <ul className="space-y-2">
            {reports.map((report) => (
              <li key={report.id} className="flex items-center justify-between p-3 border rounded">
                <div>
                  <p className="font-medium">{report.name}</p>
                  <p className="text-sm text-gray-500">
                    Created: {report.date} • Size: {report.size}
                  </p>
                </div>
                <div className="flex space-x-2">
                  <Button variant="outline" size="sm">
                    <Download className="h-4 w-4" />
                  </Button>
                  <Button variant="outline" size="sm" onClick={() => deleteReport(report.id)}>
                    <Trash2 className="h-4 w-4 text-red-500" />
                  </Button>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500 dark:text-gray-300">No reports available.</p>
        )}
      </div>
    </div>
  );
};

export default Reports;
