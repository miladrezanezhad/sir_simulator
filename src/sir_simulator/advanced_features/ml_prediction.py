"""
Machine Learning Prediction for Epidemic Forecasting
====================================================
Predict future cases using ML models (Random Forest, XGBoost)
"""

import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


class EpidemicPredictor:
    """
    Predict future epidemic cases using machine learning
    """

    def __init__(self, model_type="random_forest"):
        """
        Initialize predictor

        Parameters:
        - model_type: 'random_forest' or 'xgboost'
        """
        self.model_type = model_type
        self.model = None

        if model_type == "random_forest":
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        elif model_type == "xgboost":
            try:
                import xgboost as xgb

                self.model = xgb.XGBRegressor(n_estimators=100, random_state=42)
            except ImportError:
                print("XGBoost not installed. Using Random Forest instead.")
                self.model = RandomForestRegressor(n_estimators=100, random_state=42)
                self.model_type = "random_forest"

    def create_features(self, data):
        """
        Create time-based features from historical data

        Parameters:
        - data: DataFrame with 'day' and 'cases' columns

        Returns:
        - DataFrame with features
        """
        if isinstance(data, pd.Series):
            df = pd.DataFrame({"cases": data.values})
            df["day"] = range(len(df))
        elif isinstance(data, pd.DataFrame):
            if "cases" in data.columns:
                df = data[["day", "cases"]].copy()
            else:
                df = pd.DataFrame({"day": range(len(data)), "cases": data.values})
        else:
            df = pd.DataFrame({"day": range(len(data)), "cases": data})

        # Create lag features
        for lag in range(1, 8):
            df[f"lag_{lag}"] = df["cases"].shift(lag)

        # Create rolling averages
        df["rolling_mean_3"] = df["cases"].rolling(window=3).mean()
        df["rolling_mean_7"] = df["cases"].rolling(window=7).mean()

        # Create day features
        df["day_of_week"] = df["day"] % 7
        df["week"] = df["day"] // 7

        return df.dropna()

    def prepare_data(self, data):
        """
        Prepare data for training

        Returns:
        - X: features
        - y: target
        - df: feature DataFrame
        """
        df = self.create_features(data)

        feature_cols = [col for col in df.columns if col not in ["cases", "day"]]
        X = df[feature_cols]
        y = df["cases"]

        return X, y, df

    def train(self, data, test_size=0.2):
        """
        Train the ML model

        Parameters:
        - data: historical cases data
        - test_size: proportion for testing

        Returns:
        - metrics: dict with R² and RMSE
        - predictions: predictions on test set
        - model: trained model
        """
        X, y, df = self.prepare_data(data)

        if len(X) < 10:
            raise ValueError(f"Need at least 10 data points, got {len(X)}")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)

        metrics = {
            "r2": r2_score(y_test, y_pred),
            "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
            "train_size": len(X_train),
            "test_size": len(X_test),
        }

        return metrics, y_pred, self.model

    def predict_future(self, data, days=30):
        """
        Predict future cases

        Parameters:
        - data: historical cases data
        - days: number of days to predict

        Returns:
        - predictions: Series of future predictions
        """
        historical_df = self.create_features(data)

        # Get last row of features
        last_row = historical_df.iloc[-1:].copy()

        future_predictions = []
        current_row = last_row.copy()

        for _ in range(days):
            # Predict next value
            feature_cols = [
                col for col in current_row.columns if col not in ["cases", "day"]
            ]
            pred = self.model.predict(current_row[feature_cols])[0]
            future_predictions.append(pred)

            # Update current row for next prediction
            current_row["cases"] = pred
            current_row["day"] = current_row["day"].values[0] + 1

            # Update lag features
            for lag in range(7, 1, -1):
                if f"lag_{lag-1}" in current_row.columns:
                    current_row[f"lag_{lag}"] = current_row[f"lag_{lag-1}"]
            current_row["lag_1"] = pred

            # Update rolling averages
            current_row["rolling_mean_3"] = (
                pred + current_row.get("lag_1", pred) + current_row.get("lag_2", pred)
            ) / 3
            current_row["rolling_mean_7"] = (
                pred
                + current_row.get("lag_1", pred)
                + current_row.get("lag_2", pred)
                + current_row.get("lag_3", pred)
                + current_row.get("lag_4", pred)
                + current_row.get("lag_5", pred)
                + current_row.get("lag_6", pred)
            ) / 7

        return pd.Series(future_predictions, name="predictions")


if __name__ == "__main__":
    # Generate sample data
    historical = pd.DataFrame(
        {"day": range(1, 101), "cases": 10 + np.cumsum(np.random.poisson(0.5, 100))}
    )

    predictor = EpidemicPredictor("random_forest")
    metrics, pred, model = predictor.train(historical)
    print(f"R²: {metrics['r2']:.3f}")
    print(f"RMSE: {metrics['rmse']:.3f}")

    future = predictor.predict_future(historical, days=30)
    print(f"Future predictions: {future.values[:5]}...")
