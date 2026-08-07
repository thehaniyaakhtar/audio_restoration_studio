import matplotlib.pyplot as plt
import librosa.display
import numpy as np

# Drawing the Waveform
def save_waveform(audio, sr, output_path):
    plt.figure(figsize = (12, 4))
    
    librosa.display.waveshow(
        audio,
        sr = sr
    )
    
    plt.title("Audio Waveform")
    
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    
    plt.tight_layout()
    
    plt.savefig(output_path)
    
    plt.close()

def save_spectrogram(audio, sr, output_path):

    spectrogram = librosa.amplitude_to_db(
    np.abs(librosa.stft(audio)), # computes short time fourier transform
    ref=np.max
)

    plt.figure(figsize=(12,4))

    librosa.display.specshow(
        spectrogram,
        sr=sr,
        x_axis="time",
        y_axis="hz"
    )

    plt.colorbar(format="%+2.0f dB")

    plt.title("Spectrogram")

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()