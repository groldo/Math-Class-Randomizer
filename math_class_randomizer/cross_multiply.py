import openai
from excersise import Excersise


class CrossMultiplyEx(Excersise):
    def __init__(self, config, secret, count):
        super().__init__(config)
        self.secret = secret
        self.excersises = [self.make_prompt_request() for _ in range(count)]

    def make_prompt_request(self):
        openai.api_key = self.secret["openaiapi"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.config["cross_multiplication"]["openai_prompt"],
            max_tokens=200,
            temperature=1
        )
        return response.choices[0].text
