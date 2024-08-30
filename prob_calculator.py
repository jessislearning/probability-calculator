import copy
import random

class Hat:

    def __init__(self, **kwargs):
        contents = []
        for color,number in kwargs.items():
            for i in range(number):
                contents.append(color)            

    def draw(self, num_balls):
        drawn_list = []
        for n in range(num_balls):
           random_ball = random.choice(self.contents)
           self.contents.remove(random_ball)
           drawn_list.append(random_ball)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
