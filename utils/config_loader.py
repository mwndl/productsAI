from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN não foi encontrado no arquivo .env.")
    return token
