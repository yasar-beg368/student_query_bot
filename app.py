# app.py
import streamlit as st
from chatbot import answer_query

st.set_page_config(page_title="🎓 Student Query Bot (Offline)", page_icon="🤖")

st.title("🎓 Student Query Bot (Open Source)")
st.markdown("Ask me anything about your college.")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = answer_query(user_input)
        st.success("Answer:")
        st.write(response)
    else:
        st.warning("Please enter a valid question.")
