# AI Audio Restoration Studio

AI Audio Restoration Studio is a FastAPI-powered application that enhances noisy audio recordings, generates speech transcripts, visualizes audio signals, and provides AI-generated quality assessments.

The project combines Digital Signal Processing (DSP), speech recognition, and generative AI to create an end-to-end audio restoration workflow.

---

## Features

### Audio Enhancement
- Upload MP3 or WAV files
- Automatic noise reduction
- Save enhanced audio output

### Speech-to-Text
- Transcribe audio using OpenAI Whisper
- Generate downloadable transcript files

### Audio Analysis
- Calculate audio quality metrics
- Duration analysis
- RMS energy comparison
- Estimated noise reduction percentage

### Visualizations
- Original vs Enhanced Waveform Comparison
- Original vs Enhanced Spectrogram Comparison
- Noise Difference Spectrogram

### AI Assessment
- Uses Gemini API to evaluate:
  - Speech clarity
  - Noise reduction effectiveness
  - Overall audio quality
- Generates a concise professional assessment

### Downloads
- Enhanced Audio
- Transcript
- Analysis Report

---

## Tech Stack

### Backend
- FastAPI
- Python

### Audio Processing
- Librosa
- Noisereduce
- SoundFile
- NumPy

### Speech Recognition
- OpenAI Whisper

### AI Assessment
- Google Gemini API

### Visualization
- Matplotlib

### Frontend
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
audio_restoration_studio/
│
├── app/
│   ├── main.py
│   ├── pipeline.py
│   ├── audio_utils.py
│   ├── enhancer.py
│   ├── transcription.py
│   ├── visualizer.py
│   ├── metrics.py
│   ├── reporter.py
│   └── assessment.py
│
├── outputs/
│
├── sample_audio/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/thehaniyaakhtar/audio_restoration_studio.git

cd audio_restoration_studio
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## FFmpeg Installation

Whisper requires FFmpeg.

### Windows

```bash
winget install Gyan.FFmpeg
```

Verify installation:

```bash
ffmpeg -version
```

---

## Gemini API Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Generate an API key from:

https://aistudio.google.com

---

## Run Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Example Workflow

1. Upload audio file
2. Noise reduction is applied
3. Enhanced audio is generated
4. Whisper transcribes speech
5. Metrics are calculated
6. Waveforms and spectrograms are created
7. Gemini generates an audio quality assessment
8. Results are displayed in the web interface

---

## Example Output

### Metrics

```text
Duration: 20.01s
Original RMS: 0.1288
Cleaned RMS: 0.0488
Noise Reduction: 62.14%
```

### AI Assessment

```text
The audio restoration successfully enhanced the recording's quality. Speech clarity is excellent and background noise was significantly reduced, resulting in a cleaner and more professional listening experience.
```

---
## Screenshots
<img width="1012" height="845" alt="Screenshot (1607)" src="https://github.com/user-attachments/assets/9f830d52-4194-4fa4-9564-e481017c0143" />
<img width="720" height="707" alt="Screenshot (1608)" src="https://github.com/user-attachments/assets/224be200-6505-40b8-b79a-c3e437007492" />

---
## Future Improvements

- Real-time audio processing
- Speaker diarization
- Audio quality scoring dashboard
- Batch processing support
- GPU acceleration
- Advanced denoising models
- Cloud deployment
- User authentication
- Audio history tracking

---
