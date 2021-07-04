"""
Compare query (some text) to a set of movie plot desciptions.
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
engine = "babbage"


query = "Epic adventure"
# query = "Todd Phillips"



docs = []
file_list = glob.glob(os.path.join(os.getcwd(), folder, "*.txt"))
for file_path in file_list:
    with open(file_path, "r") as file:
        docs.append(file.read())


response = openai.Engine(engine).search(
    documents=docs, 
    query=query,
    max_rerank=None,
    return_metadata=True
)


# print(response)
print(query)
print()

i = 0
for doc in docs:
    print(doc)
    print(i, response["data"][i]["score"])
    print()
    i += 1
    
