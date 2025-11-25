# train_model.py
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 1. Load Data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train Model
print("Training model...")
model = LogisticRegression(max_iter=500)
model.fit(X, y)

# 3. Save Model
joblib.dump(model, "iris_model.pkl")
print("Success! Model saved as 'iris_model.pkl'")
