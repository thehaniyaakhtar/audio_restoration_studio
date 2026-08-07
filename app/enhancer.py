import noisereduction as nr

def remove_noise(audio, sr):
    cleaned_audio = nr.reduce_noise(
        y=audio,
        sr=sr
    )
    
    return cleaned_audio