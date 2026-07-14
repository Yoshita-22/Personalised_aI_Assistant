from transformers import pipeline, set_seed
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os
import re

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")
# Load GPT-2 only once when the application starts 

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
# For reproducibility
set_seed(42)


def generate_conversation_starters(
    event_themes: list[str],
    user_interests: list[str]
) -> list[str]:

    themes = ", ".join(event_themes)

    interests = (
        ", ".join(user_interests)
        if user_interests
        else "General Networking"
    )

    prompt = f"""
Generate exactly 3 short professional networking conversation starters.
Themes: {themes}
Interests: {interests}
Conversation Starters:
1.Don't use any thing like subheadings and all i want direct conversation starters.....
"""

    output = client.interactions.create(
    model="gemini-2.5-flash-lite",
    input=prompt
)
    cleaned_output = [
    re.sub(r'^\d+[.)]\s*', '', e)
      .replace('\\"', '"')
      .strip()
      .strip('"')
    for e in output.output_text.split("\n")
    if e.strip()
]
    return cleaned_output