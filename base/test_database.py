from sqlalchemy import create_engine, text, insert
from base.test import settings
from sqlalchemy.orm import sessionmaker, declarative_base

engine_test = create_engine(url=settings.DATABASE_URL)
SessionLocal_test = sessionmaker(autoflush=False, bind=engine_test)

