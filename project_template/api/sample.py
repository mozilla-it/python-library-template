import random


class Sample:
    def __init__(self):
        self.is_sample = True  # TESTING PRE-COMMIT AND TOX

    def get_sample_value(self, rand_value=random.randint(0, 100)) -> int:
        return rand_value
