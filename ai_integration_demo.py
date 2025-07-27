import os
from dotenv import load_dotenv
import openai
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in environment. check you .env file.")
openai.api_key = API_KEY