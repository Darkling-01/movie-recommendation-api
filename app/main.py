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
    return {"message": f"Media type is {preference.media_type} with actor {preference.original_name}"}

