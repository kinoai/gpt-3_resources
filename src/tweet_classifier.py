"""
Classifiy sentiment of tweets.
"""

import os
import openai
import dotenv


# load environment variables from `.env` file if it exists
# recursively searches for `.env` in all folders starting from work dir
dotenv.load_dotenv(override=True)


openai.api_key = os.getenv("OPENAI_API_KEY")
filename = 'prompts/text_classification/tweet_sentiment.txt'
engine = "curie"


with open(filename, "r") as file:
    prompt = file.read()
    print(prompt)


response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["###"]
)

print(response)
