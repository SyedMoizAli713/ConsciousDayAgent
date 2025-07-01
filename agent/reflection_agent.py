import streamlit as st
from openai import OpenAI

# ✅ Load API key from Streamlit secrets
openai_api_key = st.secrets.get("openai_api_key")

if not openai_api_key:
    raise ValueError("❌ Missing OpenAI API key in .streamlit/secrets.toml")

# ✅ Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# ✅ Function to generate reflection
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
        model="gpt-4o",  # Can also use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are an expert reflection and planning assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
