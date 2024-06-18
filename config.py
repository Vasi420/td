from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7450238136:AAEfo_zI0ERhsR9tbzd-6gypO6_NOex-T00")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority",
)
from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "10046731"
# -------------------------------------------------------------
API_HASH = "09a25ea3e558df7e5d969c144b0452d9"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = getenv("OWNER_ID", "5981008313")
SUPPORT_GRP = "the_comedy_bar"
UPDATE_CHNL = "AS_Bots_Updates"
OWNER_USERNAME = "Oxygen_420"
