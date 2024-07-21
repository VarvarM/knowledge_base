from sqlalchemy import create_engine
from base.config import settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(url=settings.DATABASE_URL_psycopg)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

