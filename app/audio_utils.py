import librosa

# Load Audio
def load_audio(path):
    audio, sr = librosa.load(
        path, 
        sr = 16000 # measurements per second
    )
    
    return audio, sr

# Making Waveform