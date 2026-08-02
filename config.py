import os
from dotenv import load_dotenv

load_dotenv("config.env")

CLIENT_ID = os.getenv("KICK_CLIENT_ID")
CLIENT_SECRET = os.getenv("KICK_CLIENT_SECRET")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")