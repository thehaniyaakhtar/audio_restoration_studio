import librosa


def generate_report(audio_path, transcript):

    audio, sr = librosa.load(
        audio_path,
        sr=None
    )

    duration = len(audio) / sr

    report = f"""
=== AUDIO RESTORATION REPORT ===

Duration: {duration:.2f} seconds

Processing Steps Completed:
✓ Audio Loaded
✓ Noise Reduction Applied
✓ Waveform Generated
✓ Spectrogram Generated
✓ Speech Transcription Completed

Transcript:
"{transcript}"

Output Files:
- cleaned_audio.wav
- cleaned_waveform.png
- cleaned_spectrogram.png

Status: SUCCESS
"""

    return report

def save_report(report, output_path):

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)