from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import shutil
import os

from app.pipeline import process_audio

app = FastAPI(
    title="AI Audio Restoration Studio"
)

app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)

@app.get("/")
def home():

    return {
        "message": "AI Audio Restoration Studio Running"
    }


@app.post("/process")
async def process(file: UploadFile = File(...)):

    input_path = f"sample_audio/{file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    results = process_audio(
        input_path
    )

    return results