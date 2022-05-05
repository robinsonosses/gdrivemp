from logging import debug
from gdrive import GoogleDrive
from gdrive import GoogleDriveConfig


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import FilePath
from starlette.responses import RedirectResponse

import os
app = FastAPI()

google_conf = {
    "CLIENT_ID_JSON" : "credentials.json",
    "SCOPES": [
        "https://www.googleapis.com/auth/drive"
        ],
    
}

config = GoogleDriveConfig(**google_conf)

gdrive = GoogleDrive(config)


@app.get("/")
def home():
    return RedirectResponse(url="/docs")

@app.get("/search-in-doc/{word}")
async def search(word: str):
    f = await gdrive.search(q= "fullText contains '"+word+"'" )
    return JSONResponse(status_code=200, content=f)

@app.post("/file")
async def upload_file(filename: str, filepath: str, desc_name: str):
    print(filename)
    resp = await gdrive.upload_file(    
        filename = filename,
        filepath = filepath,
        desc_name= desc_name
    )
    return JSONResponse(status_code=200, content=resp)
