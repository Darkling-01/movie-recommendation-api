from fastapi import FastAPI
from app.routes.movies import router as movie_router
from pydantic import BaseModel

app = FastAPI()

app.include_router(movie_router)


# asking for user input
class PreferenceInput(BaseModel):

    media_type: str
    original_name: str

@app.post("/preferences/")
async def set_preference(preference: PreferenceInput):
    media_type = preference.media_type

    if media_type == "movie" or media_type == "Movie":
        return {"message": f"Type: {preference.media_type} with Actor: {preference.original_name}"}
    elif media_type == "tv" or media_type == "TV":
        return {"message": f"Type: {preference.media_type} with Actor: {preference.original_name}"}
    else:
        return {"message": "Invalid Response."}

