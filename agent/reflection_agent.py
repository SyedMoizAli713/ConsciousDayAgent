import os
from openai import OpenAI

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)

def generate_reflection(journal, intention, dream, priorities):
    prompt = f"""
    You are a daily reflection and planning assistant. Your goal is to:
    1. Reflect on the user's journal and dream input
    2. Interpret the user's emotional and mental state
    3. Understand their intention and 3 priorities
    4. Generate a practical, energy-aligned strategy for their day

    INPUT:
    Morning Journal: {journal}
    Intention: {intention}
    Dream: {dream}
    Top 3 Priorities: {priorities}

    OUTPUT:
    1. Inner Reflection Summary
    2. Dream Interpretation Summary
    3. Energy/Mindset Insight
    4. Suggested Day Strategy (time-aligned tasks)
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
import os
from openai import OpenAI

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)
