import matplotlib.pylot as plt
import librosa.display

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