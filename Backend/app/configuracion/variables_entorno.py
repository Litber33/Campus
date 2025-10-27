import os
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv('DB_USER', 'root')
DB_PASS = os.getenv('DB_PASS', 'DM2024')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_NAME = os.getenv('DB_NAME', 'campus_virtual')
DB_PORT = os.getenv('DB_PORT', '3306')

SECRET_KEY = os.getenv('SECRET_KEY', 'DilanDaniel12345')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '120'))
