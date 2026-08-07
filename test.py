from app.audio_utils import load_audio
from app.visualizer import (
    save_waveform,
    save_spectrogram
)

 # Loading audio and visualization
audio, sr = load_audio(
    "sample_audio/sample.mp3"
)

save_waveform(
    audio,
    sr,
    "outputs/waveform.png"
)

save_spectrogram(
    audio,
    sr,
    "outputs/spectrogram.png"
)

print("Visualization complete!")

# Loading audio and performing noise reduction
from app.audio_utils import (
    load_audio,
    save_audio
)

from app.visualizer import (
    save_waveform,
    save_spectrogram
)

from app.enhancer import (
    remove_noise
)

audio, sr = load_audio(
    "sample_audio/sample.mp3"
)

cleaned_audio = remove_noise(
    audio,
    sr
)

save_audio(
    "outputs/cleaned_audio.wav",
    cleaned_audio,
    sr
)

save_waveform(
    cleaned_audio,
    sr,
    "outputs/cleaned_waveform.png"
)

save_spectrogram(
    cleaned_audio,
    sr,
    "outputs/cleaned_spectrogram.png"
)

print("Restoration complete!")