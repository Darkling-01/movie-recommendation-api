import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+asyncpg://darkling:Gamer0077Dark@localhost/movie_API"

# Async engine for query operations
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Sync engine for table creation
sync_engine = create_engine(DATABASE_URL, echo=True)

# Session maker for async operations
async_session = sessionmaker(
                  bind=async_engine, class_=AsyncSession, expire_on_commit=False)

# Creates base clss which SQLAlchemy models will inherit
Base = declarative_base()

class UserPreference(Base):
    __tablename__  = "user_preference"

    id = Column(Integer, primary_key=True, index=True)
    media_type = Column(String, nullable=True)
    actor_name = Column(String, nullable=True)
    original_language = Column(String, nullable=True)
    known_for_department = Column(String, nullable=True)


# Dependency to get session
#async def get_session():
#    async with AsyncSessionLocal() as session:
#        yield session

# Dependency for getting the async session
#def get_session():
#    return async_session()

def create_tables():
    # Use sync engine only to create tables
    Base.metadata.create_all(bind=sync_engine)

