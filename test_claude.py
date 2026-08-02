from anthropic import Anthropic

from src.config.settings import (
    CLAUDE_API_KEY,
    LLM,
)

client = Anthropic(api_key=CLAUDE_API_KEY)

response = client.messages.create(

    model=LLM["model"],

    temperature=0.0,

    max_tokens=50,

    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: Claude connection successful"
        }
    ]
)

print(response.content[0].text)