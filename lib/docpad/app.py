import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI(title="docpad-api")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs", status_code=301)


@app.get("/health")
async def health():
    return {"response": "docpad api is healthy"}