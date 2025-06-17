import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
        self.safe_copy = copy.deepcopy(self.contents)

    def draw(self, number_of_balls):
        self.contents = copy.deepcopy(self.safe_copy)
        if number_of_balls >= len(self.contents):
            return self.contents
        else:
            random_list = []
            self.contents = copy.deepcopy(self.contents)
            for _ in range(number_of_balls):
                drawn_ball_index = random.randint(0, len(self.contents) - 1)
                drawn_ball = self.contents.pop(drawn_ball_index)
                random_list.append(drawn_ball)
            return random_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    nominator = 0
    denominator = 0
    for _ in range(num_experiments):
        drawn_list = hat.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if drawn_list.count(key) >= value:
                balls_exist = True
            else:
                balls_exist = False
                break
        if balls_exist:
            nominator = nominator + 1
        denominator = denominator + 1
        
    probability = nominator / denominator
    return probability