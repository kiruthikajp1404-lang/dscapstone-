impogiyrt pandas as pd
import numpy as np

# Training baseline stats (replace with real values if needed)
TRAIN_STATS = {
    "RatingsCount_mean": 5000,
    "AverageRating_mean": 4.0
}

#  Define function FIRST
def detect_input_drift(new_data_df, threshold=0.2):
    drift_report = {}

    for feature in ["RatingsCount", "AverageRating"]:
        train_mean = TRAIN_STATS[f"{feature}_mean"]
        new_mean = new_data_df[feature].mean()

        drift = abs(new_mean - train_mean) / train_mean

        if drift > threshold:
            drift_report[feature] = "Drift Detected"
        else:
            drift_report[feature] = "No Drift"

    return drift_report


# Call function at bottom
if __name__ == "__main__":
    new_data = pd.DataFrame({
        "RatingsCount": [8000, 9000, 10000],
        "AverageRating": [4.2, 4.3, 4.1]
    })

    result = detect_input_drift(new_data)
    print("Drift Report:", result)

    #run this command in  new terminal  ---> .\.venv\Scripts\python.exe monitoring.py

import pandas as pd
import numpy as np

TRAIN_STATS = {
    "RatingsCount_mean": 5000,
    "AverageRating_mean": 4.0
}

def detect_input_drift(new_data_df, threshold=0.2):
    drift_report = {}

    for feature in ["RatingsCount", "AverageRating"]:
        train_mean = TRAIN_STATS[f"{feature}_mean"]
        new_mean = new_data_df[feature].mean()

        drift = abs(new_mean - train_mean) / train_mean

        if drift > threshold:
            drift_report[feature] = "Drift Detected"
        else:
            drift_report[feature] = "No Drift"

    return drift_report


# NEW FUNCTION
def should_retrain(drift_report):
    if "Drift Detected" in drift_report.values():
        return True
    return False


if __name__ == "__main__":
    new_data = pd.DataFrame({
        "RatingsCount": [8000, 9000, 10000],
        "AverageRating": [4.2, 4.3, 4.1]
    })

    drift_result = detect_input_drift(new_data)
    print("Drift Report:", drift_result)

    if should_retrain(drift_result):
        print("⚠ Drift detected! Model retraining required.")
    else:
        print("✅ Model is stable. No retraining needed.")