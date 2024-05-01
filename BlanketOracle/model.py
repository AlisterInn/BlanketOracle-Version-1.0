from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(X, y):
  model = LinearRegression()
  #Here the model traning is happening.
  model.fit(X, y)

  return model

def evaluate_model(model, X, y):
  # Here the prediction is happening
  predictions = model.predict(X)

  mse = mean_squared_error(y, predictions)


  print(f"Mean Squared Error (MSE): {mse:.2f}")
