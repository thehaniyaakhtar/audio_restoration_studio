from app.audio_utils import load_audio
from app.visualizer import (
    save_waveform,
    save_spectrogram
)

audio, sr = load_audio(
    "sample_audio/sample.mp3"
)

save_waveform(
    audio,
    sr,
    "waveform.png"
)

save_spectrogram(
    audio,
    sr,
    "spectrogram.png"
)

print("Visualization complete!")