import math
import random
import numpy as np

def get_distance(first_point, second_point):
    """
    get a distance of two points
    """
    x1 = first_point['axis_x']
    y1 = first_point['axis_y']
    x2 = second_point['axis_x']
    y2 = second_point['axis_y']
    return math.hypot (x2-x1, y2-y1)

def brute_force(points, points_count):
    """
    Find the shortest distance between two points, implements a brute force
    algorithm where all points are check.
    """
    outer_index = 0
    inner_index = 0
    shortest_distance = 99999999
    for outer_index in range (0, points_count):
        for inner_index in range ((outer_index+1), points_count):
            if get_distance(points[outer_index], points[inner_index]) < shortest_distance:
                shortest_distance = get_distance(points[outer_index], points[inner_index])
    return shortest_distance

def divide_and_conquer(points_x, points_y, points_count):
    """
    Function to recursively find the shortest distance between two points.
    the functions implements a divide and conquer methodology, it also creates
    two sets of points, one set sorted by axis x and the second sorted by axis y
    """
    shortest_distance = 0

    #if number of points is low enough, run a brute force algorithm
    if points_count <= 3:
        return brute_force(points_x, points_count)

    #implement divide and coquer, find middle point of axis_x array
    middle = int (points_count / 2)
    print (middle, points_x[middle-1])

    #divide axis_y array based in the middle point of axis_x array
    values_left = []
    values_right = []
    for point in np.nditer(points_y):
        if point['axis_x'] <= points_x[middle-1]['axis_x']:
            values_left.append(point)
        else:
            values_right.append(point)

    #create new set of arrays
    left_pts_x, right_pts_x = np.array( np.split(points_x, [middle]) )
    left_pts_y =  np.array(values_left)
    right_pts_y = np.array(values_right)

    print ("left arrays: {} -- {}".format(left_pts_x, left_pts_y))
    print ("right arrays: {} -- {}".format(right_pts_x, right_pts_y))
    #recursive find shortest distance of left and right side
    shortest_distance_left = divide_and_conquer(left_pts_x, left_pts_y, left_pts_x.size)
    shortest_distance_right = divide_and_conquer(right_pts_x, right_pts_y, right_pts_x.size)

    return min (shortest_distance_left, shortest_distance_right)


### Main Logic ###
#Create a random set of points
point = [('axis_x', int), ('axis_y', int)]
values = [(2, 3), (12, 30), (40, 50), (5, 1), (12 ,10), (3, 4)]
#points = np.array(np.random.randint(random.randint(0, 99999), size=(random.randint(2, 6), 2)), point)
points = np.array(values, point)
#random_points = np.random.randint(random.randint(0, 99999), size=(random.randint(2, 99999), 2))#np.array( random.randrange(10, 15) * np.random.random_sample((random.randrange(10, 15), 2)) - 0 )
points_count = int(points.size / points[0].size)
print ("Number of points: {}".format(points_count))
print ("Array of points: {}".format(points))

#split array of points into two, one array sorted by 'X' and the second sorted by 'Y'
points_x = np.sort(points, kind='stable', order='axis_x')
print ("Points sorted by X: {}".format(points_x))

points_y = np.sort(points, kind='stable', order='axis_y')
print ("Points sorted by Y: {}".format(points_y))

#find closest pair
print (divide_and_conquer(points_x, points_y, points_count))
