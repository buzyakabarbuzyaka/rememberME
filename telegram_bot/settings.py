import os
from os.path import join, dirname
from dotenv import load_dotenv

secret_path = join(dirname(__file__), '.secret')
load_dotenv(secret_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
