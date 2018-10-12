
"""
    Algorithm for finding the closest pairs of 2-D points.
    Given a random number points within a 2-D area find the pair of point with the shortest distance.
    The 2-D area is limited to 0 - 100 per side
"""

import random
import math
#from posix.time cimport clock_gettime, timespec, CLOCK_REALTIME

""""
    Global Variables
"""
point_list = []             #list of points
#cdef timespec ts
#cdef double current

class point:
    """
        point within the 2D area, each point has two values (x-axis, y-axis).
        a point is consider a duplicate is both axis have the same value.
    """
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def __eq__(self, other_point):
        #print ("Comparing x1,y1:{},{} and x2,y2:{},{}".format(self.x_axis, self.y_axis, other_point.x_axis, other_point.y_axis))
        if self.x_axis == other_point.x_axis:
            if self.y_axis == other_point.y_axis:
                return True
        return False

    def getDistance(self, second_point):
        x1 = self.x_axis
        y1 = self.y_axis
        x2 = second_point.x_axis
        y2 = second_point.y_axis
        print("{}-{}, {}-{}".format(x2,x1,y2,y1))
        return math.hypot (x2-x1, y2-y1)


def findShortestDistance():
    """
        traverse list of points and find shortest distance.
        find shortest distance by brute force, compare all points and calculate distance.
    """
    outer_index = 0
    inner_index = 0
    shortest_distance = 0
    for outer_index in range (0, len(point_list)):
        for inner_index in range ((outer_index+1), len(point_list)):
            """calculate distance"""
            #print ( point_list[outer_index].getDistance(point_list[inner_index]) )
            if outer_index == 0: #if first comparation, assume shortest
                shortest_distance = point_list[outer_index].getDistance(point_list[inner_index])
                #print ("shortest distance: {}".format(shortest_distance))
            else:
                if shortest_distance > point_list[outer_index].getDistance(point_list[inner_index]):
                    shortest_distance = point_list[outer_index].getDistance(point_list[inner_index])
                    #print ("shortest distance: {}".format(shortest_distance))

    print ("shortest distance: {}".format(shortest_distance))




def removeDuplicates():
    """
        traverse the list of points and remove duplicates.
    """
    outer_index = 0
    inner_index = 0
    dup_point = []
    """Identify duplicate points"""
    for outer_index in range (0, len(point_list)):
        for inner_index in range ((outer_index+1), len(point_list)):
            if point_list[outer_index] == point_list[inner_index]:
                dup_point.append(point_list[outer_index])

    """remove duplicates"""
    for duplicate in dup_point:
        #print ("duplicate point: {}".format(duplicate))
        point_list.remove(duplicate)

def showList():
    for point in point_list:
        print (point.x_axis, point.y_axis)

def createRandomPoint(points_count):
    """
        create a random number of points, use random default function.
        each axis can have a value between 0 - 100
    """
    point_list.clear()
    while points_count > 0:
        #Create a random point
        x_value = random.randrange(0,100)
        y_value = random.randrange(0,100)
        #print ("{},{}".format(x_value, y_value))
        new_point = point(x_axis=x_value, y_axis=y_value)
        point_list.append(new_point)
        points_count -= 1

def main():
    """
        find shortest distance between two points.
        The Algorithm will have 100 iterations with a random number of points on each iteration.
            10 > points_count < 1000
    """
    for iteration in range (0, 1):
        points_count = random.randrange(10, 20)
        print ("Creating {} random points".format(points_count))
        #create random points
        createRandomPoint(points_count)
        # point_list.append(point(x_axis=5, y_axis=5))
        # point_list.append(point(x_axis=5, y_axis=5))
        # point_list.insert(4, point(x_axis=9, y_axis=9))
        # point_list.insert(6, point(x_axis=9, y_axis=9))
        #check for duplicates
        removeDuplicates()
        showList()

        #set up complete start analysis
        #TODO add Time
        # clock_gettime(CLOCK_REALTIME, &ts)
        # current = ts.tv_sec + (ts.tv_nsec / 1000000000.)
        # print (current)

        findShortestDistance()
