import os
from dotenv import load_dotenv

load_dotenv()

required_vars = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]

for var in required_vars:
    if os.getenv(var) is None:
        raise ValueError(f"Variável de ambiente {var} não definida.")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "name": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}