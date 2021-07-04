"""
Compare text to a set of movie plot desciptions.
"""

import openai
import dotenv
import os
import glob


# load environment variables from `.env` file if it exists
# recursively searches for `.env` in all folders starting from work dir
dotenv.load_dotenv(override=True)


openai.api_key = os.getenv("OPENAI_API_KEY")
folder = 'prompts/semantic_search/movies/'
engine = "curie"


query = "Epic adventure"


docs = []
file_list = glob.glob(os.path.join(os.getcwd(), folder, "*.txt"))
i = 0
for file_path in file_list:
    with open(file_path, "r") as file:
        docs.append(file.read())
        print(i, "\"" + docs[-1] + "\"\n")
        i += 1


response = openai.Engine(engine).search(
    documents=docs, 
    query=query,
    max_rerank=None,
    return_metadata=True
)


print(response)
