import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from scipy import stats

class AnomalyDetector:
    """Detects anomalies in datasets using statistical & ML-based methods"""
    
    def __init__(self, df):
        self.df = df
        self.anomalies = {}

    def detect_z_score_anomalies(self, threshold=3):
        """Detects anomalies using the Z-score method"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        anomalies = {}

        for col in numeric_cols:
            z_scores = np.abs(stats.zscore(self.df[col]))
            anomalies[col] = self.df[z_scores > threshold][col].tolist()

        return anomalies

    def detect_isolation_forest_anomalies(self, contamination=0.05):
        """Detects anomalies using Isolation Forest (unsupervised ML)"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        anomalies = {}

        if len(numeric_cols) == 0:
            return {}

        model = IsolationForest(contamination=contamination, random_state=42)
        model.fit(self.df[numeric_cols])

        self.df["anomaly_score"] = model.decision_function(self.df[numeric_cols])
        self.df["is_anomaly"] = model.predict(self.df[numeric_cols])  # -1 = anomaly, 1 = normal

        for col in numeric_cols:
            anomalies[col] = self.df[self.df["is_anomaly"] == -1][col].tolist()

        self.df.drop(["anomaly_score", "is_anomaly"], axis=1, inplace=True)
        return anomalies

    def get_all_anomalies(self):
        """Runs both detection methods & combines results"""
        z_score_anomalies = self.detect_z_score_anomalies()
        isolation_forest_anomalies = self.detect_isolation_forest_anomalies()

        # Merge results from both methods
        for col in z_score_anomalies:
            if col in isolation_forest_anomalies:
                self.anomalies[col] = list(set(z_score_anomalies[col] + isolation_forest_anomalies[col]))
            else:
                self.anomalies[col] = z_score_anomalies[col]

        for col in isolation_forest_anomalies:
            if col not in self.anomalies:
                self.anomalies[col] = isolation_forest_anomalies[col]

        return self.anomalies
