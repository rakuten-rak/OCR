from fastapi import FastAPI,File,UploadFile
import shutil

import pytesseract

app = FastAPI()


@app.post('/ocr')
def ocr(image:UploadFile = File(...)):
    """working with ocr"""
    filePath = "imageTxtFile"
    with open (filePath,"w+b") as buff:
        shutil.copyfileobj(image.file, buff)
    return pytesseract.image_to_string(filePath,lang="eng")

