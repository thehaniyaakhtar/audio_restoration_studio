from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import shutil
import os

from app.pipeline import process_audio


app = FastAPI(
    title="AI Audio Restoration Studio"
)

# Create folders if missing
os.makedirs("sample_audio", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

templates = Jinja2Templates(
    directory="templates"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/process")
async def process(file: UploadFile = File(...)):

    input_path = (
        f"sample_audio/{file.filename}"
    )

    with open(
        input_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    results = process_audio(
        input_path
    )

    return results