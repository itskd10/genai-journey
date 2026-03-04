import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Demonstrate temperature effects on model output
print("=== Low Temperature (0.2) - Focused Output ===")
try:
    response_low = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Complete: what is s3",
        config={"temperature": 0.0}
    )
    print(response_low.text)
except Exception as e:
    if "RESOURCE_EXHAUSTED" in str(e):
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")

print("\nWaiting before next request...")
time.sleep(2)

# Medium temperature - balanced
print("\n=== Medium Temperature (0.7) - Balanced Output ===")
try:
    response_med = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Complete: what is s3",
        config={"temperature": 0.7}
    )
    print(response_med.text)
except Exception as e:
    if "RESOURCE_EXHAUSTED" in str(e):
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")

print("\nWaiting before next request...")
time.sleep(2)

# High temperature - more creative
print("\n=== High Temperature (1.5) - Creative Output ===")
try:
    response_high = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Complete: what is s3",
        config={"temperature": 1.5}
    )
    print(response_high.text)
except Exception as e:
    if "RESOURCE_EXHAUSTED" in str(e):
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")

print("\n" + "="*50)
print("CREATIVE TEST - Temperature Effects Visible Here")
print("="*50)

print("\n=== Low Temperature (0.0) - Focused/Predictable ===")
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write one short creative sentence about AI",
        config={"temperature": 0.0}
    )
    print(response.text)
except Exception as e:
    if "RESOURCE_EXHAUSTED" in str(e):
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")

time.sleep(2)

print("\n=== High Temperature (1.5) - Creative/Random ===")
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write one short creative sentence about AI",
        config={"temperature": 1.5}
    )
    print(response.text)
except Exception as e:
    if "RESOURCE_EXHAUSTED" in str(e):
        print("Quota exceeded. Wait before retrying.")
    else:
        print(f"Error: {e}")