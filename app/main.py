""" The script with main app """
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    return {"file_name": file.filename}
