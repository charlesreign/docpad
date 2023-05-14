from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from lib.docpad.routers import auth
from lib.docpad.routers import get_user
from fastapi.middleware.cors import CORSMiddleware
from config.config import settings

app = FastAPI(title="Docpad-Api")

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=['Auth'], prefix='/api/v1/auth')
app.include_router(get_user.router, tags=['Users'], prefix='/api/v1/users')

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs", status_code=301)

@app.get("/health")
async def health():
    return {"response": "Docpad Api is healthy"}