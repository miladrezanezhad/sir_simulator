"""
Machine Learning Prediction for Epidemics
=========================================
Predict future cases using ML algorithms
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, TimeSeriesSplit
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

class EpidemicPredictor:
    """
    Machine learning model to predict epidemic spread
    """
    
    def __init__(self, model_type='random_forest', lookback_days=7, predict_days=7):
        self.model_type = model_type
        self.lookback_days = lookback_days
        self.predict_days = predict_days
        self.model = self._create_model()
        self.scaler = StandardScaler()
        self.feature_names = None
        
    def _create_model(self):
        if self.model_type == 'random_forest':
            return RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
        elif self.model_type == 'xgboost':
            try:
                from xgboost import XGBRegressor
                return XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
            except:
                return RandomForestRegressor(n_estimators=100, random_state=42)
        else:
            return GradientBoostingRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
    
    def create_features(self, data):
        df = pd.DataFrame({'cases': data})
        
        for lag in range(1, self.lookback_days + 1):
            df[f'lag_{lag}'] = df['cases'].shift(lag)
        
        for window in [3, 7, 14]:
            df[f'rolling_mean_{window}'] = df['cases'].rolling(window).mean()
            df[f'rolling_std_{window}'] = df['cases'].rolling(window).std()
        
        df['daily_change'] = df['cases'].diff()
        df['weekly_change'] = df['cases'].diff(7)
        df['day_of_cycle'] = np.arange(len(df)) % 7
        
        df = df.bfill().ffill().fillna(0)
        return df
    
    def prepare_data(self, data):
        df = self.create_features(data)
        df['target'] = df['cases'].shift(-self.predict_days)
        df = df.dropna()
        
        feature_cols = [col for col in df.columns if col not in ['cases', 'target']]
        self.feature_names = feature_cols
        
        return df[feature_cols].values, df['target'].values, df
    
    def train(self, data, test_size=0.2):
        X, y, _ = self.prepare_data(data)
        
        if len(X) < 10:
            return None, None, None
        
        split_idx = int(len(X) * (1 - test_size))
        if split_idx < 1:
            split_idx = 1
            
        X_train, X_test = X[:split_idx], X[split_idx:]
        y_train, y_test = y[:split_idx], y[split_idx:]
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        self.model.fit(X_train_scaled, y_train)
        
        train_pred = self.model.predict(X_train_scaled)
        test_pred = self.model.predict(X_test_scaled)
        
        metrics = {
            'train_mae': mean_absolute_error(y_train, train_pred),
            'train_rmse': np.sqrt(mean_squared_error(y_train, train_pred)),
            'train_r2': r2_score(y_train, train_pred),
            'test_mae': mean_absolute_error(y_test, test_pred),
            'test_rmse': np.sqrt(mean_squared_error(y_test, test_pred)),
            'test_r2': r2_score(y_test, test_pred)
        }
        
        return metrics, test_pred, y_test
    
    def predict_future(self, historical_data, days_to_predict=30):
        predictions = []
        current_data = historical_data.copy()
        
        for _ in range(days_to_predict):
            X, _, _ = self.prepare_data(current_data)
            if len(X) == 0:
                break
            
            last_features = X[-1:].copy()
            last_features_scaled = self.scaler.transform(last_features)
            next_pred = self.model.predict(last_features_scaled)[0]
            predictions.append(max(0, next_pred))
            current_data = np.append(current_data, next_pred)
        
        return np.array(predictions)
    
    def feature_importance(self):
        if hasattr(self.model, 'feature_importances_') and self.feature_names:
            return dict(zip(self.feature_names, self.model.feature_importances_))
        return None

def generate_training_data():
    """Generate synthetic epidemic curve for training"""
    np.random.seed(42)
    t = np.arange(200)
    peak = 500
    peak_day = 80
    cases = peak * np.exp(-((t - peak_day) ** 2) / 800)
    cases = cases + np.random.normal(0, 10, len(t))
    return np.maximum(cases, 0)

if __name__ == "__main__":
    data = generate_training_data()
    predictor = EpidemicPredictor()
    metrics, pred, actual = predictor.train(data)
    if metrics:
        print(f"Test R² = {metrics['test_r2']:.3f}")
        future = predictor.predict_future(data, 30)
        print(f"30-day forecast peak: {future.max():.0f}")