import os
import streamlit as st
from openai import OpenAI

# ✅ Load the API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai_api_key"])

def generate_reflection(journal, intention, dream, priorities):
    prompt = f"""
    You are a daily reflection and planning assistant.
    Journal: {journal}
    Intention: {intention}
    Dream: {dream}
    Priorities: {priorities}
    Provide a thoughtful reflection and actionable strategy.
    """

    response = client.chat.completions.create(
        model="gpt-4o",   # or "gpt-3.5-turbo" if you want cheaper
        messages=[
            {"role": "system", "content": "You are a helpful journaling assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
