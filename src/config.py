import os

from dotenv import load_dotenv

PATH_TO_PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PATH_TO_ENV = os.path.join(PATH_TO_PROJECT, '.env')

load_dotenv(PATH_TO_ENV)

DB_URL = os.getenv('DB_URL')

PLAYER_BOT_TOKEN = os.getenv("PLAYER_BOT_TOKEN")