import os
from os.path import join, dirname
from dotenv import load_dotenv

secret_path = join(dirname(__file__), '.secret')
load_dotenv(secret_path)

TOKEN = os.environ.get("TOKEN")
