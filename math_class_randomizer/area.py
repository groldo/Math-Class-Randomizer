import random


class AreaEx():
    def __init__(self, config):
        self.excersises = [self.get_random_area()
                           for _ in range(config["area"]["count"])]

    def get_random_area(self):
        """
        Returns a random x and y value
        and two multiples of that value.
        size values are used for the actual area in the latex.
        vals are a multiple for class
        """
        randval = random.randrange(10, 100, 10)
        xsize = random.randint(3, 10)
        ysize = random.randint(3, 10)
        valdict = {
            "xsize": xsize,
            "ysize": ysize,
            "xval": xsize * randval,
            "yval": ysize * randval
        }
        return valdict
