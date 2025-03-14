from fastapi import FastAPI
from app.routes.movies import router as movie_router

app = FastAPI()

app.include_router(movie_router)

