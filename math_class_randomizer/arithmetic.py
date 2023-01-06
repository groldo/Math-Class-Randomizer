import random
from excersise import Excersise


class ArithmeticEx(Excersise):

    def __init__(self, config, count):
        super().__init__(config)
        self.excersises = [self.get_random_ex_values(
            2) for _ in range(count)]

    def get_random_ex_values(self, count) -> tuple:
        return [random.randrange(self.config["arithmetic"]["min"], self.config["arithmetic"]["max"]) for _ in range(count)]
