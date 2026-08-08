import numpy as np

def calculate_metrics(
    original_audio,
    cleaned_audio,
    sr
):

    duration = len(original_audio) / sr

    original_rms = np.sqrt(
        np.mean(original_audio ** 2)
    )

    cleaned_rms = np.sqrt(
        np.mean(cleaned_audio ** 2)
    )

    reduction_percent = (
        (original_rms - cleaned_rms)
        / original_rms
    ) * 100

    return {
        "duration": round(duration, 2),
        "original_rms": round(float(original_rms), 4),
        "cleaned_rms": round(float(cleaned_rms), 4),
        "noise_reduction_percent": round(
            float(reduction_percent),
            2
        )
    }