import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

class AdvancedModelTrainer:
    """Trains and optimizes machine learning models with hyperparameter tuning"""

    def __init__(self, X, y, test_size=0.2, random_state=42):
        self.X = X
        self.y = y
        self.test_size = test_size
        self.random_state = random_state
        self.models = {
            "linear": LinearRegression(),
            "decision_tree": DecisionTreeRegressor(),
            "random_forest": RandomForestRegressor()
        }
        self.param_grids = {
            "decision_tree": {"max_depth": [5, 10, 20]},
            "random_forest": {"n_estimators": [10, 50, 100], "max_depth": [5, 10, 20]}
        }

    def train_and_optimize(self, model_type="linear"):
        """Train and optimize the selected model"""
        if model_type not in self.models:
            raise ValueError(f"Unsupported model type: {model_type}")

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=self.test_size, random_state=self.random_state
        )

        model = self.models[model_type]

        # Perform hyperparameter tuning if applicable
        if model_type in self.param_grids:
            param_grid = self.param_grids[model_type]
            grid_search = GridSearchCV(model, param_grid, cv=5, scoring="r2", n_jobs=-1)
            grid_search.fit(X_train, y_train)
            best_model = grid_search.best_estimator_
            best_params = grid_search.best_params_
        else:
            best_model = model
            best_model.fit(X_train, y_train)
            best_params = {}

        # Make predictions
        y_pred = best_model.predict(X_test)

        # Compute performance metrics
        metrics = {
            "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
            "R2_Score": r2_score(y_test, y_pred)
        }

        return best_model, best_params, metrics
