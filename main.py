# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

import pdfplumber

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Service is up"}

@app.post("/parse/pdf")
async def parse_pdf(file: UploadFile = File(...)):
    with pdfplumber.open(file.file) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return JSONResponse(content={"text": text})
