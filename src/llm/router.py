from src.llm.client import ClaudeClient
from src.llm.parser import LLMParser
from src.llm.prompt_builder import PromptBuilder


class LLMRouter:

    def __init__(self):

        self.builder = PromptBuilder()

        self.client = ClaudeClient()

        self.parser = LLMParser()

    def run(self, context):

        system_prompt, user_prompt = self.builder.build(
            context
        )

        response = self.client.generate(
            system_prompt,
            user_prompt,
        )

        context.llm_result = self.parser.parse(
            response
        )

        return context