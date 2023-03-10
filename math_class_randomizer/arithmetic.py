import random
from excersise import Excersise


class ArithmeticEx(Excersise):

    def __init__(self, config):
        super().__init__(config)
        self.excersises = [self.get_random_ex_values(
            2) for _ in range(self.config["count"])]

    def get_random_ex_values(self, count) -> tuple:
        """
        Returns a list of randomly generated values from the given range.
        The number of values returned can be controlled by the `count` parameter.
        """
        return [
            random.randrange(self.config["min"], self.config["max"]+1)
            for _ in range(count)
        ]
