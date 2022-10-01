import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME")
OWNER_ID = getenv("OWNER_ID")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/de91427fe131a0578cfb4.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/de91427fe131a0578cfb4.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Sumit9969/NIXA-MUSIC-BOT")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/100b3e9f1c6fd5c360009.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/99759e89c31a3fe414dd9.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/8f2f9b83e4420dd2f3cca.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/f41a7e3ceed3b088e14e5.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/4b767e04d236fec02ca55.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/41a53b4571a0b90b2fd5c.jpg")
