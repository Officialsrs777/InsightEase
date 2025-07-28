
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv() 

def summarize_meeting(transcript_path: str) -> str:
    
    api_key = os.getenv("SONAR_API_KEY") 
    if not api_key:
        sys.exit("Error: SONAR_API_KEY not found. Please set it in .env or hard‑code it above.")

    
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    
    endpoint = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "sonar-pro",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes meeting transcripts."
            },
            {
                "role": "user",
                "content": (
                    "Please provide a concise, bullet‑point summary of the following meeting transcript:\n\n"
                    + transcript
                )
            }
        ]
    }

   
    resp = requests.post(endpoint, headers=headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python ai_integration_demo.py <transcript.txt>")
        sys.exit(1)

    summary = summarize_meeting(sys.argv[1])
    print("\n=== Meeting Summary ===\n")
    print(summary)

if __name__ == "__main__":
    main()
