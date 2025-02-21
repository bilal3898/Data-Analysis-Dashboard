from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
import optuna

class AdvancedModelTrainer:
    """Handles hyperparameter tuning & model selection"""

    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.models = {}
        self.best_model = None

    def train_and_optimize(self, model_type="random-forest"):
        """Performs hyperparameter tuning & model selection"""

        def objective(trial):
            if model_type == "random-forest":
                params = {
                    "n_estimators": trial.suggest_int("n_estimators", 100, 1000),
                    "max_depth": trial.suggest_int("max_depth", 5, 50),
                    "min_samples_split": trial.suggest_int("min_samples_split", 2, 20)
                }
                model = RandomForestRegressor(**params)

            elif model_type == "gradient-boosting":
                params = {
                    "n_estimators": trial.suggest_int("n_estimators", 100, 1000),
                    "learning_rate": trial.suggest_loguniform("learning_rate", 1e-3, 1),
                    "max_depth": trial.suggest_int("max_depth", 3, 10)
                }
                model = GradientBoostingRegressor(**params)

            elif model_type == "neural-network":
                params = {
                    "hidden_layer_sizes": trial.suggest_categorical("hidden_layer_sizes", [(100,), (100, 50), (100, 50, 25)]),
                    "activation": trial.suggest_categorical("activation", ["relu", "tanh"]),
                    "learning_rate": trial.suggest_categorical("learning_rate", ["constant", "adaptive"])
                }
                model = MLPRegressor(**params)

            # Train model
            model.fit(self.X, self.y)
            return -model.score(self.X, self.y)

        # Run optimization
        study = optuna.create_study(direction="minimize")
        study.optimize(objective, n_trials=50)

        # Get best parameters
        best_params = study.best_params

        # Train final model with best parameters
        if model_type == "random-forest":
            self.best_model = RandomForestRegressor(**best_params)
        elif model_type == "gradient-boosting":
            self.best_model = GradientBoostingRegressor(**best_params)
        elif model_type == "neural-network":
            self.best_model = MLPRegressor(**best_params)

        self.best_model.fit(self.X, self.y)

        # Store model & metrics
        metrics = {"best_score": study.best_value}
        return self.best_model, best_params, metrics
