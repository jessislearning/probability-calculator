import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color,number in kwargs.items():
            for i in range(number):
                self.contents.append(color)            

    def draw(self, num_balls):
        drawn_list = []
        if num_balls > len(self.contents):
            drawn_list = copy.copy(self.contents)
            self.contents.clear()
            return drawn_list
        
        for n in range(num_balls):
           random_ball = random.choice(self.contents)
           self.contents.remove(random_ball)
           drawn_list.append(random_ball)
        return drawn_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0

    for i in range(num_experiments):
        color_match = 0
        hat_reset = copy.deepcopy(hat)
        draw = hat_reset.draw(num_balls_drawn)
      
        #Uncomment to see what balls are drawn and what are expected:
        #print(f'\n\n--DRAW-- {draw}')
        #print(f'Balls we want to match: {expected_balls}')

        for color, number in expected_balls.items():
            balls_per_color=0

            for ball in draw:
                if (color==ball):
                    balls_per_color+=1
            #print(f'{color} balls: {balls_per_color}')

            if balls_per_color >= number:
                color_match+=1
                 
        if color_match == len(expected_balls):
            matches+=1

        #print(f'matches so far : {matches}')

    probability = matches/num_experiments
    #print (f'probability= {probability}\nnumber of experiments: {num_experiments}\nmatches: {matches}\n')
    return probability

