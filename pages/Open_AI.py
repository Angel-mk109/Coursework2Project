from openai import OpenAI
from pip._internal.cli.cmdoptions import python

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='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')
# Make a simple API call
completion = client.chat.completions.create(
model="gpt-4o",
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Hello! What is AI?"}
]
)
print(completion.choices[0].message.content)