"""
Find shortest distance of a pair of points among a set of multiple points within a 2-D plane
Given a random number points within a 2-D area find the pair of point with the shortest distance.
implement divide a conquer algorithm until the number of points to process gets to lower bound then
implement a brute force algorithm to fin the shortest distance
"""

import csv
import sys
import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt #pylint: disable=import-error

def get_distance(first_point, second_point):
    """
    get a distance of two points
    """
    axis_x1 = first_point['axis_x']
    axis_y1 = first_point['axis_y']
    axis_x2 = second_point['axis_x']
    axis_y2 = second_point['axis_y']
    return math.hypot(axis_x2-axis_x1, axis_y2-axis_y1)

def brute_force(points_list, list_count):
    """
    Find the shortest distance between two points, implements a brute force
    algorithm where all points are check.
    """
    outer_index = 0
    inner_index = 0
    shortest_distance = 99999999
    for outer_index in range(0, list_count):
        for inner_index in range((outer_index+1), list_count):
            distance = get_distance(points_list[outer_index], points_list[inner_index])
            if distance != 0 and distance < shortest_distance:
                shortest_distance = get_distance(points_list[outer_index], points_list[inner_index])
    return shortest_distance

def divide_and_conquer(points_x, points_y, points_count):
    """
    Function to recursively find the shortest distance between two points.
    the functions implements a divide and conquer methodology, it also creates
    two sets of points, one set sorted by axis x and the second sorted by axis y
    """
    shortest_distance = 0

    #if number of points is low enough, run a brute force algorithm
    if points_count <= 200: #arbitrary value
        return brute_force(points_x, points_count)

    #implement divide and coquer, find middle point of axis_x array
    middle = int(points_count / 2)

    #divide axis_y array based in the middle point of axis_x array
    values_left = []
    values_right = []
    for point in np.nditer(points_y):
        if point['axis_x'] <= points_x[middle]['axis_x']:
            values_left.append(point)
        else:
            values_right.append(point)

    #create new set of arrays
    left_pts_x, right_pts_x = np.array(np.split(points_x, [middle]))
    left_pts_y = np.array(values_left)
    right_pts_y = np.array(values_right)

    print("left arrays: {} -- {}".format(left_pts_x, left_pts_y))
    print("right arrays: {} -- {}".format(right_pts_x, right_pts_y))
    #recursive find shortest distance of left and right side
    shortest_distance = min(divide_and_conquer(left_pts_x, left_pts_y, left_pts_x.size),
                            divide_and_conquer(right_pts_x, right_pts_y, right_pts_x.size))

    #check the middle of the 2-D plane, and figure out if the shortest distance
    #is on one of the points there
    middle_values = []
    for point in np.nditer(points_y):
        if abs(point['axis_x'] - points_x[middle]['axis_x']) < shortest_distance:
            middle_values.append(point)
    strip_points = np.array(middle_values)

    #run a brute force to find the shortest distance within the strip
    return min(shortest_distance, brute_force(strip_points, strip_points.size))


def save_results(points_count, total_time):
    """
    save results into a text file
    comma separate format (csv)
    """
    out_filename = "results.txt"
    file = open(out_filename, "a+")

    line = str(points_count) + "," + str(total_time) + "\n"
    file.write(line)
    file.close()

def create_graph(graph_type):
    """
    display the results into a graph
    """
    axis_x = []
    axis_y = []

    #open file and read line
    in_filename = "results.txt"
    file = open(in_filename, "r")
    for line in csv.reader(file):
        axis_x.append(line[0])
        axis_y.append(line[1])
    file.close()

    # plot with various axes scales
    plt.figure(1, figsize=(10, 10))

    # log
    if graph_type == 0:
        plt.subplot(222)
        plt.plot(axis_x, axis_y)
        plt.yscale('log')
    #exponential
    else:
        plt.subplot(223)
        plt.plot(axis_x, axis_y)
        plt.xscale('log')

    plt.ylabel("Time")
    plt.xlabel("Number of Points")
    plt.title('Time Complexity Analysis')
    plt.grid(True)
    plt.show()

def get_constants():
    results = []
    constants = np.array([1, 1, 1])
    aux = 0
    #open file and read line
    in_filename = "results.txt"
    file = open(in_filename, "r")
    for line in csv.reader(file):
        result = []
        #results.append(int(line[0]))
        result.append(float(line[0]))
        result.append(float(line[1]))
        results.append(result)
        aux += 1
        if aux == 3:
            break
    file.close()
    results = np.array(results)

    print ("results: {}".format(results))
    print ("vector {}".format(constants))
    print ("Ax=b {}".format(constants.dot(results)))

### Main Logic ###
if __name__ == "__main__":
    for run in range(2, 1000): #arbitray values
        print("-----------------------------------------------------------------------------------")
        #Create a random set of points
        random.seed(19680801) #set to reproducibility
        POINT = [('axis_x', int), ('axis_y', int)]
        VALUES = [(random.randint(0, 200), random.randint(0, 200)) for coordinate in range(run)]

        ##points = np.array(np.random.randint(random.randint(0, 99999),
        #size=(random.randint(2, 6), 2)), POINT)
        POINTS = np.array(VALUES, POINT)
        POINTS_COUNT = int(POINTS.size / POINTS[0].size)
        print("Number of points: {}".format(POINTS_COUNT))
        print("Array of points: {}".format(POINTS))



        brute = 0
        graph = 0
        try:
            if len(sys.argv) == 2 and sys.argv[1] == "brute_force":
                brute = 1
                graph = 1
        except ValueError:
            pass

        #split array of points into two, one array sorted by 'X' and the second sorted by 'Y'
        POINTS_X = np.sort(POINTS, kind='stable', order='axis_x')
        print("Points sorted by X: {}".format(POINTS_X))

        if brute == 1:
            #set up complete start analysis
            START_TIME = time.time()
            SHORTEST_DISTANCE = brute_force(POINTS_X, POINTS_COUNT)
            #stop timer
            END_TIME = time.time()
            TOTAL_TIME = END_TIME-START_TIME
        else:
            POINTS_Y = np.sort(POINTS, kind='stable', order='axis_y')
            print("Points sorted by Y: {}".format(POINTS_Y))

            #set up complete start analysis
            START_TIME = time.time()
            #find closest pair
            SHORTEST_DISTANCE = divide_and_conquer(POINTS_X, POINTS_Y, POINTS_COUNT)
            #stop timer
            END_TIME = time.time()
            TOTAL_TIME = END_TIME-START_TIME



        #save results
        save_results(POINTS_COUNT, TOTAL_TIME)
        print("Shortest Distance: {}".format(SHORTEST_DISTANCE))
        print("Found in: {}".format(TOTAL_TIME))

    #calculate constants
    get_constants()
    #plot data
    create_graph(graph)
