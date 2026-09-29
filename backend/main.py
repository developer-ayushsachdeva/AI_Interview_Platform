from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.interview import router as interview_router

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application with a custom title and description.",
    version="1.0.0"
)

# CORS configuration middleware laga rhe  
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://ai-mockinterview-platform.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(interview_router)
