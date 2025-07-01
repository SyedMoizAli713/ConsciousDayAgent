import streamlit as st
import os

st.write("Current working directory:", os.getcwd())
st.write("Loaded secret:", st.secrets.get("openai_api_key", "❌ Not found"))

import streamlit as st
from openai import OpenAI

# Load OpenAI API key from Streamlit secrets
openai_api_key = st.secrets.get("openai_api_key")

if not openai_api_key:
    st.error("❌ Missing OpenAI API key! Please add it to .streamlit/secrets.toml")
    st.stop()


# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Function to generate reflection
def generate_reflection(journal, intention, dream, priorities):
    prompt = f"""
You are a daily reflection and planning assistant.
Given the following inputs:

Morning Journal: {journal}
Dream: {dream}
Intention: {intention}
Top 3 Priorities: {priorities}

Please generate a thoughtful reflection and a brief actionable strategy for the day.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert reflection and planning assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# --- Streamlit UI ---
st.set_page_config(page_title="🪞 Conscious Day Planner", layout="centered")
st.title("🪞 Daily Reflection & Planner")
st.write("Write your thoughts and get a focused plan for the day.")

with st.form("reflection_form"):
    journal = st.text_area("🌅 Morning Journal", height=150)
    dream = st.text_input("💭 What did you dream about?")
    intention = st.text_input("🎯 Today's intention")
    priorities = st.text_input("✅ Top 3 Priorities (comma-separated)")

    submitted = st.form_submit_button("Generate Reflection")

if submitted:
    with st.spinner("Generating your reflection..."):
        try:
            output = generate_reflection(journal, intention, dream, priorities)
            st.success("Here’s your reflection and plan:")
            st.markdown(output)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
