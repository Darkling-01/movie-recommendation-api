import sqlalchemy
from sqlalchemy.ext.delcarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://darkling:Gamer0077Dark@localhost/movie_API"

# Async database connection
database = Database(DATABASE_URL)

# Sync database connection (for non-async usage)
engine = sqlachemy.create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

