from fastapi import APIRouter
from app.utils.external_api import get_movie_recommendations

router = APIRouter()

# @ are decorator functions that modify or enhance the behavior of 
# other functions without changing code directly

@router.get("/media/allresults")   # route handler

# async functions run concurrently and are ideal for API call
async def movie_recommendations():
    media_data = await get_movie_recommendations()
    if "movie" in media_data:
        return {"movie":media_datail}
    else:
        return media_data

# Receiving user's preferences by using GET to searh through collection
@router.get("/media/filtering")

async def filtering_user_input(actor_name: str=None):
    media_data = await get_movie_recommendations()
    # Apply filtering logic
    filtered_data = []

    # filter data based on media type and actor
    for media in media_data:
       try:
           if isinstance(media, dict):
               if actor_name and media.get("original_name") == actor_name:
                   filtered_data.append(media)
           else:
               print(f"Skipping non-dictionary item: {media}")   # Debugging
       except AttributeError as e:
            print(f"Unexpected Error occurred: {e}")
            continue

    return {"filtered results": filtered_data} 
