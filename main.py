"""
Main execution script.
Run this file to train and evaluate the model.
"""

from src.data_preprocessing import load_data, clean_data, split_features_target
from src.train import train_model, save_model
from src.evaluate import evaluate_model


DATA_PATH = "data/crude_data.xlsx"
MODEL_PATH = "models/crude_inlet_model.pkl"


def main():
    print("Loading data...")
    df = load_data(DATA_PATH)

    print("Cleaning data...")
    df = clean_data(df)

    print("Splitting features and target...")
    X, y = split_features_target(df)

    print("Training model...")
    model, X_test, y_test = train_model(X, y)

    print("Evaluating model...")
    metrics = evaluate_model(model, X_test, y_test)

    print("\nModel Performance:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\nSaving model...")
    save_model(model, MODEL_PATH)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
