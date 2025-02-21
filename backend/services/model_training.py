from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

class ModelTrainer:
    """Handles machine learning model training & evaluation"""
    
    def __init__(self, df, target_column, feature_columns, model_type="linear"):
        self.df = df
        self.target_column = target_column
        self.feature_columns = feature_columns
        self.model_type = model_type
        self.model = None
        self.scaler = StandardScaler()
        
    def prepare_data(self):
        """Prepares training and testing datasets"""
        X = self.df[self.feature_columns]
        y = self.df[self.target_column]
        
        # Standardize features
        X_scaled = self.scaler.fit_transform(X)
        
        # Split data into train & test sets
        return train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
    def train(self):
        """Trains the selected ML model"""
        X_train, X_test, y_train, y_test = self.prepare_data()
        
        # Choose model based on type
        if self.model_type == "linear":
            self.model = LinearRegression()
        elif self.model_type == "decision-tree":
            self.model = DecisionTreeRegressor(random_state=42)
        elif self.model_type == "random-forest":
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        
        # Compute model evaluation metrics
        metrics = {
            "r2": r2_score(y_test, y_pred),
            "mse": mean_squared_error(y_test, y_pred),
            "accuracy": self.model.score(X_test, y_test)  # Accuracy for regression
        }
        
        # Compute feature importance if applicable
        if self.model_type in ["decision-tree", "random-forest"]:
            importance = self.model.feature_importances_
        else:
            importance = np.abs(self.model.coef_)
            
        feature_importance = dict(zip(self.feature_columns, importance))
        
        return metrics, feature_importance

    def predict(self, input_features):
        """Generates predictions for new data"""
        input_scaled = self.scaler.transform([input_features])
        return self.model.predict(input_scaled).tolist()
