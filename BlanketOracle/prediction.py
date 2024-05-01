def predict_temperature(model, outdoor_temp):
  features = [[outdoor_temp]]

  # Making predictions using the model.
  predicted_temp = model.predict(features)[0]

  return predicted_temp

def recommend_blanket(predicted_temp):
  thresholds = {
      "heavy": 14,  # Below this temperature, recommend a HEAVY blanket
      "medium": 27,  # Between this and light, recommend a MEDIUM blanket
      "light": None,  # Above this, recommend a LIGHT blanket
  }

  for blanket_type, threshold in thresholds.items():
    if threshold is None or predicted_temp < threshold:
      return blanket_type

  return "light" 
