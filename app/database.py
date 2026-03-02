from sqlalchemy import create_engine
from app.config import DB_CONFIG

def get_engine():
    connection_string = (
        f"postgresql://{DB_CONFIG['user']}:"
        f"{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/"
        f"{DB_CONFIG['name']}"
    )

    return create_engine(connection_string, echo=False)