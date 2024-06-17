from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7450238136:AAGTQ3HPoxp5CobIRFeEZ_C61_pf7XUtYEM")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority",
)
