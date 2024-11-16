import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')
GOOGLE_CREDENTIALS = os.getenv('GOOGLE_CREDENTIALS')

# Constants
MAX_RETRIES = 3
RATE_LIMIT_DELAY = 1  # seconds
MAX_RESULTS_PER_SEARCH = 5

# File handling
ALLOWED_EXTENSIONS = ['.csv']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# LLM settings
DEFAULT_MODEL = "gpt-4"
MAX_TOKENS = 1000
TEMPERATURE = 0.7