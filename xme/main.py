from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from global_router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(router, prefix="/api")