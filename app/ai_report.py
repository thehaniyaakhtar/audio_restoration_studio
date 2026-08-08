from google import genai

client = genai.Client()


def generate_ai_summary(
    transcript,
    metrics
):

    prompt = f"""
You are an audio analysis expert.

Transcript:
{transcript}

Metrics:
{metrics}

Generate a professional
audio restoration summary.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text