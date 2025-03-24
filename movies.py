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
               # If actor_name is provided, filter by actor_name
               if actor_name and actor_name.lower() not in media.get("original_name", "").lower():
                   continue   # Skip this result if actor_name has no match

               # If media_type is provided, filter by media_type in the "known for" list
               if media_type:
                   media_type_match = False  # Flag to track if a match is found in known_for
                   for known_item in media.get("known_for", []):  # Loop over "known_for" list
                         if known_item.get("media_type", "").lower() == media_type.lower():
                             media_type_match = True   # Set flag to True if match is found
                             break  # Exit the loop once a match is found
                   if not media_type_match:  # If no match is found, continue to the next item
                        continue
  
               if original_language:
                   original_language_match = False
                   for known_item in media.get("known_for", []):
                        known_language = known_item.get("original_language", "").lower()
                        if known_language == original_language.lower():
                            original_language_match = True
                            break
                   if not original_language_match:
                       continue
 
               if known_for_department:
                   department_match = False
                   for known_item_department in media.get("known_for", []):
                        department = known_item_department.get("known_for_department", "").lower()
                        if department == known_for_department.lower():
                           department_match = True
                           break
                   if not department_match:
                       continue

               filtered_data.append(media)   # Add the media iteam to the filtered results
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


