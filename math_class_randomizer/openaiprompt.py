import openai


class OpenAIPrompt():
    def __init__(self, secret):
        self.secret = secret

    def make_prompt_request(self, prompt):
        openai.api_key = self.secret
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=1
        )
        return response.choices[0].text