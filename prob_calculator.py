import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color,number in kwargs.items():
            for i in range(number):
                self.contents.append(color)            

    def draw(self, num_balls):
        drawn_list = []
        if num_balls > len(self.contents):
            return self.contents
        
        for n in range(num_balls):
           random_ball = random.choice(self.contents)
           self.contents.remove(random_ball)
           drawn_list.append(random_ball)
        return drawn_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    experiments = 0
    expected_balls_list = []

    for key,value in expected_balls.items():
        for n in range(value):
            expected_balls_list.append(key)

    for i in range(num_experiments):
        color_true = 0
        hat_reset = copy.deepcopy(hat)
        draw = hat_reset.draw(num_balls_drawn)
        #print(f'\n\n--DRAW-- {draw}')
        #print(f'Expected Balls: {expected_balls}')
        for color, number in expected_balls.items():
            ball_count_color=0

            for ball in draw:
                if (color==ball):
                    ball_count_color+=1
            #print(f'{color} ball count: {ball_count_color}')

            if ball_count_color >= number:
                color_true+=1
                #print (f'color_true so far: {color_true}')    
        if color_true == len(expected_balls):
            matches+=1
        #print(f'target value: {len(expected_balls)}')     
        #print(f'matches = {matches}')
        experiments +=1

    probability = matches/experiments
    #print (f'probability= {probability}')
    return probability
    #print(f'number of experiments: {experiments}\nmatches: {matches}\n')

#hat1 = Hat(blue=5, red=5, green=5)
#experiment(hat1, {"red": 1, "blue": 1}, num_balls_drawn=3, num_experiments=100)

#hat = Hat(black=6, red=4, green=3)
#probability = experiment(hat=hat,
#                  expected_balls={'red':2,'green':1},
#                  num_balls_drawn=5,
#                  num_experiments=2000)
