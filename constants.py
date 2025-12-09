from dotenv import load_dotenv
import os

DEFAULT_PADDING = (10,  10, 10, 10)

load_dotenv()
API_KEY = os.getenv("API_KEY")