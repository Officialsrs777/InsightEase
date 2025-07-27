import os
from dotenv import load_dotenv
import openai
from openai.error import RateLimitError

# Load and validate API key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "Missing OPENAI_API_KEY in environment. Check your .env file."
    )
openai.api_key = API_KEY

def summarize_meeting(
    transcript: str,
    model: str = "gpt-3.5-turbo",
    max_tokens: int = 500,
    temperature: float = 0.2
) -> str:
    """
    Returns a bullet-point summary of key points and action items.
    If quota is exceeded, returns a friendly warning.
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
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    except RateLimitError:
        return (
            "⚠️ Unable to generate summary: insufficient OpenAI quota. "
            "Please check your billing settings at "
            "https://platform.openai.com/account/billing."
        )

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Summarize a meeting transcript via OpenAI"
    )
    parser.add_argument(
        "transcript_file",
        help="Path to a text file containing the meeting transcript"
    )
    args = parser.parse_args()

    # Read the transcript
    with open(args.transcript_file, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    # Generate and print the summary
    result = summarize_meeting(transcript_text)
    print("\n===== INSIGHTEASE SUMMARY =====\n")
    print(result)
    print("\n==============================\n")
