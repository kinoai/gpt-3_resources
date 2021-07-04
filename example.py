import openai

import dotenv
import os

# load environment variables from `.env` file if it exists
# recursively searches for `.env` in all folders starting from work dir
dotenv.load_dotenv(override=True)


api_key = os.environ['OPENAI_API_KEY']
