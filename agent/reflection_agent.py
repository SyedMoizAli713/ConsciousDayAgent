import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with Streamlit Secrets
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENAI_API_KEY"],
)

def generate_reflection(journal, intention, dream, priorities):
    prompt = f"""
    You are a daily reflection and planning assistant...
    """

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "https://consciousdayagent.streamlit.app",
            "X-Title": "ConsciousDayAgent",
        },
        model="openai/gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    
    return completion.choices[0].message.content
