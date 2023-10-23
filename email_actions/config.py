import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')

load_dotenv(dotenv_path=dotenv_path)

DB_HOST_NAME = os.getenv('DB_HOST_NAME')
DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
EMAIL_ID = os.getenv('EMAIL_ID')