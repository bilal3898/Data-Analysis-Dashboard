from transformers import pipeline
import pandas as pd
import numpy as np
from scipy import stats

class InsightGenerator:
    """Generates AI-powered insights from datasets"""
    
    def __init__(self, df):
        self.df = df
        self.insights = []
        
    def generate_statistical_insights(self):
        """Extracts key statistics and trends"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            mean = self.df[col].mean()
            trend = self.df[col].diff().mean()
            z_scores = np.abs(stats.zscore(self.df[col]))
            anomalies = self.df[col][z_scores > 3]
            
            if len(anomalies) > 0:
                self.insights.append(f"⚠️ {len(anomalies)} anomalies detected in '{col}'")
            
            if trend > 0:
                self.insights.append(f"📈 '{col}' shows an increasing trend ({trend:.2f} per period)")
            elif trend < 0:
                self.insights.append(f"📉 '{col}' shows a decreasing trend ({trend:.2f} per period)")
    
    def generate_correlation_insights(self):
        """Identifies strong relationships between variables"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        corr_matrix = self.df[numeric_cols].corr()
        
        for i in range(len(numeric_cols)):
            for j in range(i+1, len(numeric_cols)):
                corr = corr_matrix.iloc[i, j]
                if abs(corr) > 0.7:
                    self.insights.append(
                        f"🔗 Strong {'positive' if corr > 0 else 'negative'} correlation "
                        f"({corr:.2f}) between '{numeric_cols[i]}' and '{numeric_cols[j]}'"
                    )
                    
    def generate_ai_summary(self):
        """Uses AI to generate a textual summary of the dataset"""
        summarizer = pipeline("summarization")
        text_description = self.df.describe().to_string()
        summary = summarizer(text_description, max_length=150, min_length=50)
        self.insights.append(f"🤖 AI Summary: {summary[0]['summary_text']}")
        
    def get_all_insights(self):
        """Runs all insight generation methods"""
        self.generate_statistical_insights()
        self.generate_correlation_insights()
        self.generate_ai_summary()
        return self.insights
