import librosa
import soundfile as sf

# Load Audio
def load_audio(path):
    audio, sr = librosa.load(
        path, 
        sr = 16000 # measurements per second
    )
    
    return audio, sr

# Saving cleaned audio files
def save_audio(path, audio, sr):
    sf.write(path, audio, sr)

