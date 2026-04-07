import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Phishing Detector", page_icon="🔐")

# Title
st.markdown("<h1 style='text-align: center;'>🔐 AI Phishing Detection System</h1>", unsafe_allow_html=True)

# Description
st.write("Enter a URL or message to check if it is safe or phishing.")

# Input box
user_input = st.text_area("Enter text here")

# Button
if st.button("🔍 Check Now"):
    if user_input:
        data = vectorizer.transform([user_input])
        result = model.predict(data)[0]

        # Confidence (basic)
        prob = model.predict_proba(data)[0]
        confidence = max(prob) * 100

        if result == "phishing":
            st.error(f"⚠️ Phishing Detected! ({confidence:.2f}% confidence)")
        else:
            st.success(f"✅ Safe Content ({confidence:.2f}% confidence)")
    else:
        st.warning("Please enter something!")
        