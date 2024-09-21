# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///sales_tracker.db'  # You can change this to your preferred database

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
