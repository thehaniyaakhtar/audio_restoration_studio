import librosa

def generate_report(
    audio_path,
    transcript
):
    audio, sr = librosa.load(
        audio_path,
        sr = None
    )
    
    duration = len(audio) / sr
    
    report = f"""
Audio Restoration Report

Duration: {duration:.2f} seconds

Noise reduction applied successfully.

Transcript:
{transcript}

Artifacts Generated:
- Waveform
- Spectrogram
- Cleaned Audio

Pipeline Completed Successfully.
    """
    
    return report
    