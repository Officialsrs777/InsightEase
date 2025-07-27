import os
from dotenv import load_dotenv
import openai
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in environment. check you .env file.")
openai.api_key = API_KEY
def summarize_meeting(transcript: str,
                      model: str = "gpt-3.5-turbo",
                      max_tokens: int = 500,
                      temperature: float = 0.2) -> str:
    """
    Returns a bullet-point summary of key points and action items.
    """
    prompt = f"""
You are an AI assistant. Summarize the following meeting transcript:

\"\"\"
{transcript}
\"\"\"

Provide:
1) A concise bullet-point summary.
2) A bullet-point list of action items.
"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message["content"].strip()
