import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_assessment(
    transcript,
    metrics
):

    prompt = f"""
You are an audio restoration expert.

Transcript:
{transcript}

Metrics:
{metrics}

Write a professional assessment in
100 words or less.

Discuss:
- speech clarity
- noise reduction effectiveness
- overall quality

Do not use bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text