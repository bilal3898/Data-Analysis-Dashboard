import React, { useState } from "react";
import { Sparkles, ChevronDown, ChevronUp, AlertCircle } from "lucide-react";

const Insights = ({ insights, anomalies }) => {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="p-6 bg-white dark:bg-gray-900 shadow-lg rounded-lg">
      <div className="flex items-center justify-between">
        <h3 className="text-xl font-semibold flex items-center">
          <Sparkles className="mr-2 text-blue-500" />
          AI Insights
        </h3>
        <button onClick={() => setExpanded(!expanded)} className="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300">
          {expanded ? <ChevronUp /> : <ChevronDown />}
        </button>
      </div>

      {insights ? (
        <div className={`mt-4 space-y-2 ${expanded ? "block" : "hidden"}`}>
          {insights.split("\n").map((line, index) => (
            <p key={index} className="text-gray-700 dark:text-gray-300">{line}</p>
          ))}
        </div>
      ) : (
        <p className="mt-4 text-gray-500 dark:text-gray-300">No insights available. Generate insights from the analysis tab.</p>
      )}

      {/* Anomaly Detection */}
      {anomalies && anomalies.length > 0 && (
        <div className="mt-4 p-4 bg-red-50 dark:bg-red-900 rounded-lg">
          <h4 className="font-semibold flex items-center">
            <AlertCircle className="mr-2 text-red-600" />
            Detected Anomalies
          </h4>
          <ul className="mt-2 text-red-600 dark:text-red-300">
            {anomalies.map((anomaly, index) => (
              <li key={index} className="text-sm">
                {`🔴 ${anomaly.date} - Amount: $${anomaly.amount}`}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Insights;
