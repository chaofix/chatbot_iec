from fastapi import FastAPI, File, UploadFile
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    data = json.loads(contents)
    return {"filename": file.filename, "data": data}
