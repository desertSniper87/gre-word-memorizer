import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gre_words.db')

# Dictionary API URL (free, no auth required)
DICTIONARY_API_BASE_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'