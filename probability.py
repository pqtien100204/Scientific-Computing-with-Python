import copy
import random
from time import time

class Hat:
    def __init__(self, **kwargs):    #**kwargs: keyworded arguments   |     *arg: non-keyword arguments
        self.kwargs = kwargs

        self.contents = []
        for key in self.kwargs.keys():
            for i in range(self.kwargs[key]):
                self.contents.append(key)
                
        # self.contents = [[key for i in range(kwargs[key])] for key in kwargs.keys()]

    # def __str__(self):
        # for key in self.kwargs.keys():
        #     for i in range(self.kwargs[key]):
        #         self.contents.append(key)
        # return str(self.contents)

    def draw(self, num_of_drawed_balls):
        self.num_of_drawed_balls = num_of_drawed_balls
        self.ls_dr_ba = list()

        if num_of_drawed_balls > len(self.contents):
            return self.contents
        elif num_of_drawed_balls <= len(self.contents):
            for time in range(num_of_drawed_balls):
                drawed_ball = random.choice(self.contents)
                self.ls_dr_ba.append(drawed_ball)

                #drawed_ball = random.randrange(len(self.contents))   # randrange: randomly select a number in a range

                self.contents.remove(drawed_ball)  #  pop() method like del deletes value at a particular index => returns deleted value from the list.
            
            return self.ls_dr_ba

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
# change the expected ball into a content list => compare the 2 content list
    # diction_contents = []
    # for key in expected_balls.keys():
    #     for i in range(expected_balls[key]):
    #         diction_contents.append(key)
    # result = [[hat.draw(num_balls_drawn)] for time_of_expe in range(num_experiments)]

    counter_for_catched_times = 0  
    for time_of_expe in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        expected_balls_copy = copy.deepcopy(expected_balls)

        gotten_words = list(hat_copy.draw(num_balls_drawn))
        print(gotten_words)
        for drawed_element in gotten_words:
            hat_copy.contents.append(drawed_element)

        dict_convert = {}
        for elemen in gotten_words:
            if elemen not in dict_convert:
                dict_convert[elemen] = 1
            else:
                dict_convert[elemen] += 1
        print(dict_convert)

# change the expected ball into a content list => compare the 2 content list
        # smaller_inside_counter = 0
        # for elem in diction_contents:
        #     if elem in hat.ls_dr_ba:
        #         smaller_inside_counter += 1
        #         hat.ls_dr_ba.remove(elem)
        #     # print(smaller_inside_counter)
        # if smaller_inside_counter == len(diction_contents):
        #     counter_for_catched_times += 1
    # print(counter_for_catched_times)

# way II: change the list of drawed word into a dictionary => compare the 2 dictionaries
        smaller_inner_counter = 0
        for k, v in dict_convert.items():
            if k in expected_balls_copy.keys():
                if dict_convert[k] >= expected_balls_copy[k]:
                    smaller_inner_counter += 1
            print(smaller_inner_counter)
        if smaller_inner_counter == len(expected_balls_copy.keys()):
            counter_for_catched_times += 1
        print(counter_for_catched_times)   

# way III: -1 in each ball of the expected ball list until the amount is 0
        # for each_color in gotten_words:
        #     if each_color in expected_balls_copy.values():
        #         expected_balls_copy[each_color] -= 1
        # print(expected_balls_copy.items())

        # smaller_inner_counter = 0
        # for x in expected_balls_copy.values():
        #     if x <= 0:
        #         smaller_inner_counter += 1 
        #     print(smaller_inner_counter)
        # if smaller_inner_counter == 3:
        #     counter_for_catched_times += 1
        # print(counter_for_catched_times) 

    #probability = f"Through {num_experiments} times of trying, we got the expected balls {counter_for_catched_times}. The prob is {counter_for_catched_times / num_experiments}"
    probability = counter_for_catched_times / num_experiments
    return probability

# TESTING
# hat1 = Hat(blue=4, red=2, green=6)
# hat2 = Hat(red=2, blue=0, purple=4, pink=1, spotted=1, brown=3)

# print(hat1.contents)
# print(hat1.draw(14))
# print(hat2.contents)
# print(hat2.draw(5))

# hat = Hat(black=6, red=4, green=3, yellow=6, apple=7)
# probability = experiment(hat, {"red":1}, 3, 4)
# print(probability)
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=10)
print(probability)