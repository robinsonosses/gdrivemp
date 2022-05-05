<h3 align="center">FastAPI Gdrive</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/MadeByMads/fastapi-cloud-drives/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>


## 🧐 About <a name = "about"></a>

The FastAPI Gdrive module supports Google Drive search & upload files.  
This proyect is forked version of https://github.com/MadeByMads/fastapi-cloud-drives


## 🏁 Getting Started <a name = "getting_started"></a>


### 🔨 Installing
with  pip
```bash
python3 -m venv .venv

source .venv/bin/activate
pip install --upgrade setuptools
python -m pip install --upgrade pip

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

pip install git+https://github.com/robinsonosses/gdrivemp

git clone https://github.com/robinsonosses/gdrivemp.git
```
<h3 align="center">FastAPI Google Drive</h3>

<div align="center">



</div>


## 🧐 About <a name = "about"></a>

The FastAPI Cloud Google Drive module supports Google Drive. You can easily search & upload files. 

### Step 1
Go to link https://developers.google.com/drive/api/v3/quickstart/python
Enable Drive Api.
Download credentials.json file

### Step 2
Before deploying app to production you need one time approve and give permission.
Run:
```python
python main.py --noauth_local_webserver
```
Follow instruction, get verification code from Google and paste it in terminal. 
After successful authentication, module will create ```storage.json``` file. 

If you change permissions in Google Cloud for the application, you need repeat Step 2 again.

### Step 3
Run application:
```python
uvicorn main:app --reload
```

### Example main.py:

```python
from logging import debug
from fastapi_cloud_drives import GoogleDrive
from fastapi_cloud_drives import GoogleDriveConfig


from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
    f = await gdrive.search(q= "fullText contains '{word}'" )
    return JSONResponse(status_code=200, content=f)

@app.post("/file")
async def upload_file(filename: str, filepath: str, desc_name: str):
    resp = await gdrive.upload_file()
    return JSONResponse(status_code=200, content=resp)
```

```CLIENT_ID_JSON``` is a file that you download from Google Cloud.
