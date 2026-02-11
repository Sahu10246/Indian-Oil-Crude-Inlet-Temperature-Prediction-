"""
Model Training Module
Builds and trains Polynomial Regression model.
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import joblib
import os


def train_model(X, y, degree: int = 2):
    """Train Polynomial Regression model."""

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = Pipeline([
        ("poly_features", PolynomialFeatures(degree=degree, include_bias=False)),
        ("linear_regression", LinearRegression())
    ])

    model.fit(X_train, y_train)

    return model, X_test, y_test


def save_model(model, path: str):
    """Save trained model."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
