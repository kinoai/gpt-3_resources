# GPT-3 Workshop Resources

## Setup

Create .env file with your OpenAI API key.

## Commands

```bash
python src/hackernews_title_generator.py

python src/tweet_classifier.py

python src/semantic_search.py
```

## API usage examples

```python
import openai
import os

# set api key
openai.api_key = os.getenv("OPENAI_API_KEY")

# list engines
engines = openai.Engine.list()

# create a completion
completion = openai.Completion.create(engine="ada", prompt="Hello world")

# print the completion
print(completion.choices[0].text)

# execute semantic search
response = openai.Engine("ada").search(
    documents=["some text 1", "some text 2", ...],
    query="some query",
    return_metadata=True
)
```

## RESOURCES

OpenAI API <br>
https://beta.openai.com

GPT-3 Apps & Products <br>
https://gpt3demo.com/map

GitHub Copilot <br>
https://copilot.github.com

Codex Javascript Sandbox <br>
https://beta.openai.com/codex-javascript-sandbox

HuggingFace Transformers Library <br>
https://huggingface.co/docs/transformers/index
