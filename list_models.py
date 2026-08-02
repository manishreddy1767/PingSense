from anthropic import Anthropic

from src.config.settings import CLAUDE_API_KEY

client = Anthropic(api_key=CLAUDE_API_KEY)

models = client.models.list()

for model in models.data:
    print(f"{model.id:<35} {model.display_name}")