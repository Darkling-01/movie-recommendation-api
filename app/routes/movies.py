from fastapi import APIRouter
from app.utils.external_api import get_movie_recommendations

router = APIRouter()

# @ are decorator functions that modify or enhance the behavior of 
# other functions without changing code directly

@router.get("/movies/recommendations")# route handler

# async functions run concurrently and are ideal for API call
async def movie_recommendations():
    movie_data = await get_movie_recommendations()
    if "movies" in movie_data:
        return {"movies":movie_data["movies"]}
    else:
        return movie_data
