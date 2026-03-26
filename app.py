# app.py
import streamlit as st
import pickle

vectorizer, model = pickle.load(open("model/model.pkl", "rb"))

st.title("🗞️ Fake News Detector")
st.write("Paste a news headline or article below:")

text = st.text_area("News text", height=200)

if st.button("Analyze"):
    if text.strip():
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]

        if pred == 1:
            st.success(f"✅ Likely REAL — {prob[1]*100:.1f}% confidence")
        else:
            st.error(f"🚨 Likely FAKE — {prob[0]*100:.1f}% confidence")
    else:
        st.warning("Please enter some text.")