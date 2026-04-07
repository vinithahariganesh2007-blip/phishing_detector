import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Take user input
text = input("Enter message or URL: ")

# Convert input
text_vector = vectorizer.transform([text])

# Predict
prediction = model.predict(text_vector)

print("Result:", prediction[0])