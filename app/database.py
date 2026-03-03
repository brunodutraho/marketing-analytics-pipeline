from sqlalchemy import create_engine
from app.config import DATABASE_URL

def get_engine():
    return create_engine(DATABASE_URL, echo=False)