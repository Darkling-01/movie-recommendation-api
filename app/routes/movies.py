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
@router.get("/media/advanced_filtering")
# Advanced search
async def filtering_user_input(
                               media_type: str=None,
                               actor_name: str=None,
                               original_language: str=None,
                               known_for_department: str=None
                              ):

    media_data = await get_movie_recommendations()

    # Make sure we're working with the "results" key from the media_data 
    results = media_data.get("results", [])
    # Apply filtering logic
    filtered_data = []

    # filter data based on media type and actor
    for media in results:
       try:

           if isinstance(media, dict):  # Only process dictonary items
               if actor_name and actor_name.lower() not in media.get("original_name", "").lower():
                   continue
               if media_type and media.get("media_type", "").lower() != media_type.lower():
                   continue
               if original_language and media.get("original_language","").lower() != original_language.lower():
                   continue
               filtered_data.append(media)
           else:
               print(f"Skipping non-dictionary item: {media}")   # Debugging
       except AttributeError as e:
           print(f"Unexpected Error occurred: {e}")
           continue
    # Return filtered results with a message if no match is found
    if filtered_data:
        return {"filtered results": filtered_data}
    else:
        return {"message": "No matching actor found. Displaying all results.", 
                "filtered_results": results}


