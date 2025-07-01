from openai import OpenAI

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
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
            "HTTP-Referer": "http://localhost:8501",  # Optional for local testing
            "X-Title": "ConsciousDayAgent",           # Optional
        },
        model="openai/gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000  # ✅ Limit token usage to stay within your credits
    )
    
    return completion.choices[0].message.content

