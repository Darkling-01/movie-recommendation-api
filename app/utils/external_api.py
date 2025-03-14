import httpx

async def get_movie_recommendations():

     url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"

     headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYWZhMDcxMzI2OTM2ZWE1NzJhYjcyNTVmZDQ2NjhhMSIsIm5iZiI6MTc0MTg5OTU2MC42NTY5OTk4LCJzdWIiOiI2N2QzNDcyOGNmYjg5OTAxOTQzMGY5YmQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ZAePHB3TKGufkn18dbQvnsxVIZO7BVvfpAy59b5Vcb4"
}

     async with httpx.AsyncClient() as client:
         response = await client.get(url, headers=headers)

     if response.status_code == 200:
        return response.json()      # Return the JSON for further processing
        movies = data.get("results",[])
     else:
        print(f"Error: {response.status_code}")
        return None
   
