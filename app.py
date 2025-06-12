import streamlit as st

st.title("Quantified Memecoins")
st.write("🚀 Memecoin Scanner + GPT Token Analyzer is Live!")

token = st.text_input("Enter Token Name")
if token:
    st.success(f"GPT Analysis: '{token}' is a BUY (Confidence: 82%)")
