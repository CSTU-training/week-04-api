import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from a .env file if present.
load_dotenv()

# Read the database connection URL from the environment.
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

# Create the SQLAlchemy engine. This manages connections and the DB dialect.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

# Create a configured "SessionLocal" class for creating session objects.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for ORM models to inherit from.
Base = declarative_base()

# FastAPI dependency that provides a DB session and ensures it is closed.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
