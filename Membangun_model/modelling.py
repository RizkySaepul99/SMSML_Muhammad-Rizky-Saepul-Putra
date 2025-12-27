import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("EAFC26_OVR_Prediction")

# Load data
df = pd.read_csv(
    r"Membangun_model\EAFC26_preprocessing.csv"
)

X = df.drop(columns=["OVR"])
y = df["OVR"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

with mlflow.start_run():
    mlflow.sklearn.autolog()

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rmse = mean_squared_error(y_test, y_pred) ** 0.5
    r2 = r2_score(y_test, y_pred)

    print("RMSE :", rmse)
    print("R^2  :", r2)