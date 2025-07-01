import os
from openai import OpenAI

# ✅ Load only from environment or Streamlit Secrets
# DO NOT put any default fallback key here

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)

def generate_reflection(journal, intention, dream, priorities):
    prompt = f"""
    ... your prompt ...
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
