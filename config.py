from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7228049154:AAGRxkbQ_dUVbVt52BjVVc9ENHtUMr-ov68")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority",
)
