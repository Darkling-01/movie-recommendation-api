import asyncio
from app.database import create_tables  # Replace with your actual function

def main():
    asyncio.run(create_tables())  # Run the async function inside an event loop

if __name__ == "__main__":
    main()

