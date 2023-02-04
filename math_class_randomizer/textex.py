from excersise import Excersise
from openaiprompt import OpenAIPrompt


class TextEx(Excersise):
    def __init__(self, config, secret):
        super().__init__(config)
        openaiprompt = OpenAIPrompt(secret)
        prompt = self.config["openai_prompt"]
        self.excersises = [
            openaiprompt.make_prompt_request(prompt)
            for _ in range(self.config["count"])
        ]
