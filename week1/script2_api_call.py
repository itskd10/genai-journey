import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("Preparing API call...")
time.sleep(2)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain GenAI in one sentence"
    )
    print(response.text)
except Exception as e:
    if "RESOURCE_EXHAUSTED" in str(e):
        print("Free tier quota exceeded. Please wait a moment before retrying.")
        print("Upgrading to paid plan will give you more quota.")
    else:
        print(f"Error: {e}")
