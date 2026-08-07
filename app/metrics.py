import numpy as np


def calculate_metrics(original_audio, cleaned_audio):

    original_rms = np.sqrt(
        np.mean(original_audio**2)
    )

    cleaned_rms = np.sqrt(
        np.mean(cleaned_audio**2)
    )

    reduction_percent = (
        (original_rms - cleaned_rms)
        / original_rms
    ) * 100

    return {
        "original_rms": float(original_rms),
        "cleaned_rms": float(cleaned_rms),
        "noise_reduction_percent": float(
            reduction_percent
        )
    }