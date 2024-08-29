import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        contents = []
        for color,number in kwargs.items():
            for i in range(number):
                contents.append(color)            

    def draw(self, num_balls):
        #contents = [ list containing balls ]
        #drawn_list = []
        #for n in num_balls:
        #   random_ball = random.choice(ball_box)
        #   ball_box.remove(random_ball)
        #   drawn_list.append(random_ball)

        pass

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
