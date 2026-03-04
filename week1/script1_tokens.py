# pip install tiktoken
import tiktoken

# See how your DE words break into tokens
encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Test with your everyday DE words
texts = [
    "AWS Glue",
    "ETL pipeline",
    "Databricks",
    "Redshift",
    "My Glue job failed",
    "Supercalifragilistic"
]

print("=" * 40)
print("TOKEN BREAKDOWN")
print("=" * 40)

for text in texts:
    tokens = encoder.encode(text)
    print(f"\nText: '{text}'")
    print(f"Token count: {len(tokens)}")
    print(f"Token IDs: {tokens}")

print("\n" + "=" * 40)
print("COST ESTIMATE (Gemini Pro)")
print("=" * 40)
sample_prompt = "Why did my AWS Glue job fail last night?"
prompt_tokens = encoder.encode(sample_prompt)
print(f"\nPrompt: '{sample_prompt}'")
print(f"Tokens: {len(prompt_tokens)}")
print(f"Gemini cost: Nearly FREE on free tier!")
