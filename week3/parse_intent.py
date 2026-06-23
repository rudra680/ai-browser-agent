import os
import json

from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT, FEW_SHOT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def parse_intent(user_command):

    prompt = f"""
{SYSTEM_PROMPT}

{FEW_SHOT}

User:
{user_command}

Output:
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleaned = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(cleaned)

    except Exception as e:

        return {
            "action": "api_error",
            "message": str(e)
        }