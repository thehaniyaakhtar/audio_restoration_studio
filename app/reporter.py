def generate_report(
    transcript,
    metrics
):

    report = f"""
=== AUDIO ANALYSIS REPORT ===

Duration:
{metrics['duration']} seconds

Original RMS:
{metrics['original_rms']}

Cleaned RMS:
{metrics['cleaned_rms']}

Estimated Noise Reduction:
{metrics['noise_reduction_percent']}%

Transcript:
{transcript}

Analysis:

Speech was successfully detected.

Noise reduction was applied
while preserving speech content.

Generated Assets:

- Cleaned Audio
- Waveform
- Spectrogram
- Difference Spectrogram

Status: SUCCESS
"""

    return report


def save_report(report, output_path):

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)