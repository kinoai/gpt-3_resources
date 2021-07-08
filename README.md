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


## Useful repos
- GPT-3 tutorial: https://github.com/bhattbhavesh91/gpt-3-simple-tutorial