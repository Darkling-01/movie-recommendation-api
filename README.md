# movie-recommendation-api

Creating a simple API to collect movie information of user's preferences and display a selection of options with advance features.
This project is design to understand the fundamental of recieving and sending API request with FastAPI libraries. 

# File Structure

``` bash
movie-recommendation-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── movies.py
│   │   ├── recommendations.py
│   │   └── ratings.py
│   └── utils/
│       ├── __init__.py
│       └── external_api.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── tests/
    ├── __init__.py
    ├── test_movies.py
    ├── test_recommendations.py
    └── test_ratings.py
```
