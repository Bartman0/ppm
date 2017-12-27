# coding: utf-8
import random
import math
import time

class PPMSimulator:

    conf_limit = 0.5

    def __init__(self, conf_limit=0.6):
        self.conf_limit = conf_limit

    def read_cars(self):
        time.sleep(1)
        return random.randint(0, 7+math.floor(1/self.conf_limit))

