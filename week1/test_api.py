import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

system_instruction = """
You are internal AI assistant
for XYZ Data Engineering team.

ONLY answer about:
- XYZ company specific pipelines
- XYZ company specific Glue jobs
- XYZ company specific S3 buckets
- XYZ company pipeline errors

ALWAYS REFUSE and say
"Please check documentation"
for these:
- General AWS questions
- General Python questions
- Non DE topics like cricket
- Anything not XYZ company specific

Keep answers under 3 lines.
Be precise and direct.
"""

def ask_company_ai(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            max_output_tokens=150
        ),
        contents=question
    )
    return response.text

# Test all scenarios
questions = [
    "When do our pipelines run?",
    "What is S3?",
    "What is cricket?",
    "Our Glue job failed, help!",
    "What is Python?",
]

print("=" * 40)
print("COMPANY AI ASSISTANT TEST")
print("=" * 40)

for q in questions:
    print(f"\nQ: {q}")
    print(f"A: {ask_company_ai(q)}")
    print("-" * 40)
# ```

# ---

# ## What You Will See Now
# ```
# Q: When do our pipelines run?
# A: XYZ pipelines run at 2AM daily.

# Q: What is S3?
# A: Please check AWS documentation
#    for general questions. I only
#    help with XYZ company specific
#    DE questions.

# Q: What is cricket?
# A: Please check documentation.
#    I only help with XYZ company
#    data engineering questions.

# Q: Our Glue job failed, help!
# A: Please share the error message
#    and I will help troubleshoot
#    your XYZ Glue job.

# Q: What is Python?
# A: Please check documentation
#    for general Python questions.
# ```

# ---

# ## The Token Problem — Solved!
# ```
# BEFORE:
# No max_output_tokens
# Gemini writes essay
# = 500+ tokens used
# = More cost ❌

# ━━━━━━━━━━━━━━━━━━━

# AFTER:
# max_output_tokens=150
# Gemini stays concise
# = 150 tokens max
# = Less cost ✅
# = Faster response ✅
# ```

# ---

# ## Golden Rule for System Prompts
# ```
# VAGUE instruction:
# "Answer only DE questions"
# → Gemini interprets loosely
# → Answers S3 general questions
# → More tokens used ❌

# ━━━━━━━━━━━━━━━━━━━

# SPECIFIC instruction:
# "REFUSE general AWS questions
#  ONLY answer XYZ company
#  specific pipeline questions"
# → Gemini follows strictly
# → Refuses general questions
# → Less tokens used ✅
# ```

# ---

# ## Important Lesson Learned Today
# ```
# System Prompt quality
# = Answer quality
#         ↓
# Bad prompt → Bad answers
# Good prompt → Good answers
#         ↓
# This is EXACTLY why
# Week 2 is entirely about
# PROMPT ENGINEERING!
#         ↓
# Writing good prompts
# is a full skill!
# Not just common sense!
# # ```

# ---

# ## What You Will See
# ```
# Q: What tools does our team use?
# A: Your team uses AWS Glue for ETL,
#    S3 for data lake and Redshift
#    as your data warehouse.

# Q: When do our pipelines run?
# A: Your pipelines run at 2AM daily.

# Q: What is cricket?
# A: I can only help with XYZ company
#    data engineering questions.
# ```

# ---

# ## This is Exactly What Companies Do!
# ```
# COMPANY A — Bank:
# System prompt tells AI:
# "You are banking assistant
#  Only answer finance questions
#  Never discuss competitors"

# COMPANY B — Hospital:
# System prompt tells AI:
# "You are medical assistant
#  Only answer health questions
#  Always recommend doctor"

# YOUR COMPANY:
# System prompt tells AI:
# "You are DE team assistant
#  Only answer pipeline questions
#  Use our AWS setup context"
# ```

# ---

# ## Your Learning Path
# ```
# TODAY — System Prompt:
# Tell AI your company context
# Takes 5 minutes
# Works immediately! ✅
#         ↓
# WEEK 6 — RAG:
# Connect AI to your
# actual company documents
# Real data answers! ✅
#         ↓
# WEEK 12 — Fine Tuning:
# Train AI specifically
# on your company style
# Expert level answers! ✅
#         ↓
# WEEK 16 — Full App:
# All 3 combined!
# Complete company AI! ✅