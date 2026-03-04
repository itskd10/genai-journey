import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("GPT_API_KEY")
client = OpenAI(api_key=api_key)

# Demonstrate temperature effects on model output
print("=== Low Temperature (0.0) - Focused Output ===")
try:
    response_low = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Complete: The capital of INDIA is"}],
        temperature=0.0
    )
    print(response_low.choices[0].message.content)
except Exception as e:
    if "rate_limit" in str(e).lower():
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")

print("\nWaiting before next request...")
time.sleep(2)

# Medium temperature - balanced
print("\n=== Medium Temperature (0.7) - Balanced Output ===")
try:
    response_med = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Complete: The capital of France is"}],
        temperature=0.7
    )
    print(response_med.choices[0].message.content)
except Exception as e:
    if "rate_limit" in str(e).lower():
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")

print("\nWaiting before next request...")
time.sleep(2)

# High temperature - more creative
print("\n=== High Temperature (1.5) - Creative Output ===")
try:
    response_high = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Complete: The capital of France is"}],
        temperature=1.5
    )
    print(response_high.choices[0].message.content)
except Exception as e:
    if "rate_limit" in str(e).lower():
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")