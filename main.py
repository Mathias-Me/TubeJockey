from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import youtube_dl
ydl_opts = {}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: Change this maybe?
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World!"}

@app.get("/download")
async def download(url):
    url = url.replace('"','')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return {"success" : "True"}

# Run by uvicorn main:app --reload