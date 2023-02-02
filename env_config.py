from os import environ, path
from dotenv import load_dotenv

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# General Config
TWITTER_USERNAME = environ.get('TWITTER_USERNAME')
TWITTER_PASSWORD = environ.get('TWITTER_PASSWORD')
QUEUE_NAME = environ.get('QUEUE_NAME')
OPENAI_API_KEY = environ.get('OPENAI_API_KEY')

# def Get_env(key=None):
#     return environ.get(key)

