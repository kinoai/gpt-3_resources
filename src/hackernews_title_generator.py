"""
Generate new titles for hackernews posts.
"""

import openai
import dotenv
import os


# load environment variables from `.env` file if it exists
# recursively searches for `.env` in all folders starting from work dir
dotenv.load_dotenv(override=True)


openai.api_key = os.getenv("OPENAI_API_KEY")
filename = 'prompts/text_generation/hackernews.txt'
engine = "curie"


with open(filename, "r") as file:
    prompt = file.read()


response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    temperature=0.95,
    max_tokens=50,
    top_p=1.0,
    frequency_penalty=0.9,
    presence_penalty=0.9,
    stop=["\n\n"],
)

print(response["choices"][0]["text"])
