from os import environ
from dotenv import load_dotenv

load_dotenv()

db_name = environ.get('DB_NAME')
db_host = environ.get('DB_HOST')
db_port = environ.get('DB_PORT')
db_user = environ.get('DB_USER')
db_pass = environ.get('DB_PASS')
