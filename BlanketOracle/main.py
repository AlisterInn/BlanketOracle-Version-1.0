from data_handler import load_data, preprocess_data
from model import train_model, evaluate_model
from prediction import predict_temperature, recommend_blanket

data = load_data()
X, y = preprocess_data(data)

model = train_model(X, y)
evaluate_model(model, X, y)

# Get outdoor temperature  from user
outdoor_temp_new = float(input("Give your outdoor temprature: "))

predicted_temp = predict_temperature(model, outdoor_temp_new)
blanket_recommendation = recommend_blanket(predicted_temp)

# Print results
print(f"Predicted indoor temperature: {predicted_temp:.2f} °C")
print(f"Blanket recommendation: ✨ Go for a pretty {blanket_recommendation} blanket!✨")
print("Happy Sleeping ᶻ 𝗓 𐰁.𖥔 ݁ ˖🛌")