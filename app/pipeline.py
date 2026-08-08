from app.audio_utils import (
    load_audio,
    save_audio
)

from app.visualizer import (
    save_waveform,
    save_spectrogram,
    save_difference_spectrogram
)

from app.enhancer import (
    remove_noise
)

from app.transcription import (
    transcribe_audio
)

from app.reporter import (
    generate_report,
    save_report
)

from app.metrics import (
    calculate_metrics
)

from app.assessment import (
    generate_assessment
)

def process_audio(input_audio_path):

    # Load audio
    audio, sr = load_audio(input_audio_path)

    # Remove noise
    cleaned_audio = remove_noise(
        audio,
        sr
    )
    
    metrics = calculate_metrics(
    audio,
    cleaned_audio,
    sr
    )

    # Save cleaned audio
    cleaned_audio_path = (
        "outputs/cleaned_audio.wav"
    )

    save_audio(
        cleaned_audio_path,
        cleaned_audio,
        sr
    )

    # Generate visualizations
    waveform_path = (
        "outputs/cleaned_waveform.png"
    )

    spectrogram_path = (
        "outputs/cleaned_spectrogram.png"
    )

    save_waveform(
        cleaned_audio,
        sr,
        waveform_path
    )

    save_spectrogram(
        cleaned_audio,
        sr,
        spectrogram_path
    )

    # Transcribe audio
    transcript = transcribe_audio(
        cleaned_audio_path
    )
    
    assessment = generate_assessment(
    transcript,
    metrics
)

    # Save transcript
    transcript_path = (
        "outputs/transcript.txt"
    )
    
    save_difference_spectrogram(
    audio,
    cleaned_audio,
    sr,
    "outputs/difference_spectrogram.png"
    )

    with open(
        transcript_path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(transcript)

    # Generate report
    report = generate_report(
    transcript,
    metrics
    )

    report_path = (
        "outputs/report.txt"
    )

    save_report(
        report,
        report_path
    )

    # Return results
    return {
        "transcript": transcript,
        "metrics": metrics,
        "report": report,
        "assessment": assessment,
        "cleaned_audio":
            "http://127.0.0.1:8000/outputs/cleaned_audio.wav",
        "waveform":
            "http://127.0.0.1:8000/outputs/cleaned_waveform.png",
        "spectrogram":
            "http://127.0.0.1:8000/outputs/cleaned_spectrogram.png",
        "difference_spectrogram":
            "http://127.0.0.1:8000/outputs/difference_spectrogram.png"
    }