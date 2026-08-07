# transcript_test.py

from app.transcription import (
    transcribe_audio
)

text = transcribe_audio(
    "outputs/cleaned_audio.wav"
)

print(text)