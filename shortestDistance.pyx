
"""
    Algorithm for finding the closest pairs of 2-D points.
    Given a random number points within a 2-D area find the pair of point with the shortest distance.
    The 2-D area is limited to 0 - 100 per side
"""

import random

""""
    Global Variables
"""
points_list = []

class point():
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

def createRandomPoint(pairs_number):
    while pairs_number > 0:
        """Create a random pair"""
        x_value = random.randrange(0,100)
        y_value = random.randrange(0,100)
        #print ("{},{}".format(x_value, y_value))
        new_point = point(x_axis=x_value, y_axis=y_value)
        points_list.append(new_point)
        pairs_number -= 1

    for pair in points_list:
        print (pair.x_axis, pair.y_axis)

def main():
    createRandomPoint(10)
