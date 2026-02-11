"""
Model Evaluation Module
Computes MAE and R² score.
"""

from sklearn.metrics import mean_absolute_error, r2_score


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return {
        "MAE": round(mae, 3),
        "R2 Score": round(r2, 4)
    }
