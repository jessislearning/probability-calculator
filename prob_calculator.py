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
    #count_true = 0
    #count_total = 0
    #for i in num_experiments:
        #hat_reset = copy.deepcopy(hat)
        #draw = hat_reset.draw(num_balls_drawn)
            #figure out how to check if expected_balls are in the draw
            #if expected_balls in draw:
                #count_true += 1
        #count_total += 1

