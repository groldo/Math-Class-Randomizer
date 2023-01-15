import datetime


class Context():
    def __init__(self, ):
        self.context = {}
        self.context["today"] = datetime.date.today().strftime(
            format="%d.%m.%Y")

    def add_to_context(self, key, value):
        self.context[key] = value
