# Your name: Berfredd Quezon
# Your Section: 11

import point
import math
from typing import Optional

# Write your functions for each part in the space below.

#Task 1 - first_element
'''
input: list of list of floats
output: list of floats
purpose: create a list containing the first element of every list in the original list
steps:
1. check if big list is empty -> return none if true
2. create empty list named new_list
3. loop through nested lists
    3.1. check if nested list is empty -> move on to next list if true
    3.2. add first element in nested list from the original list to new_list
4. return new_list
'''
def first_element(big_list:list[[list[float]]]) -> Optional[list[float]]:
    if big_list:
        new_list = []
        i = 0
        while i < len(big_list):
            if big_list[i]:  # same as if big_list[i] != []
                temp = big_list[i]
                new_list.append(temp[0])
                i += 1
            else:
                i += 1
        return new_list
    else:
        return None

# Task 2 - x_coordinates
'''
input: list of Point objects
output: list of floats
purpose: create a list with all the x coordinates from a list of point objects
steps:
1. check if list is empty -> if true return None
2. create empty list named list_x
3. loop through list
    3.1 add x element to list_x
4. return list_x
'''
def x_coordinates(list:list[point]) -> Optional[list[point]]:
    if list == []:
        return None
    list_x = []
    i = 0
    while i < len(list):
        list_x.append(list[i].x)
        i+=1
    return list_x

# Task 3 - are_in_positive_quadrant
'''
input: list of Point objects
output: list of Point objects
purpose: create a list with the points with positive x and y values
steps:
1. check if list is empty -> if true return None
2. create empty list named list_pos
3. loop through list
    3.1 add point object to list_pos
4. return list_pos
'''
def are_in_positive_quadrant(list:list[point]) -> Optional[list[point]]:
    if not list:
        return None
    list_pos = []
    i = 0
    while i < len(list):
        if list[i].x > 0 and list[i].y > 0:
            list_pos.append(list[i])
            i += 1
        else:
            i += 1
    return list_pos

# Task 4 - euclidean_distance
'''
input: two point objects
output: a float
purpose: return the euclidean distance (square root of the difference of the points squared) between two points
steps:
1. create variable to store answer
2. find the euclidean distance between the points
3. return answer
'''
def euclidean_distance(P1:point,P2:point) -> float:
    #answer = (((P1.x-P2.x)**2)+((P1.y-P2.y)**2))**0.5
    answer = math.sqrt(math.pow(P1.x-P2.x,2)+math.pow(P1.y-P2.y,2))
    return answer

# Task 5 - manhattan_distance
'''
input: two point objects
output: a float
purpose: return the euclidean distance (square root of the difference of the points squared) between two points
steps:
1. create variable to store answer
2. find the manhattan distance (sum of the absolute value of the difference between the points) between two points
3. return answer
'''
def manhattan_distance(P1:point,P2:point) -> float:
    answer = abs(P1.x-P2.x)+abs(P1.y-P2.y)
    return answer

# Task 6 - distance_all
'''
input: list of point objects
output: list of point objects
purpose: return the euclidean distance (square root of the difference of the points squared) between two points
steps:
1. check if list is empty -> if true return None
2. create a variable to act as the point 0,0
3. create an empty list named new_list to store the distance from the origin
4. loop through list
    4.1 find the euclidean distance between the point and the origin
    4.1 add the difference to the new_list
5. return new_list
'''
def distance_all(list:list[point]) -> Optional[list[float]]:
    if not list:
        return None
    origin = point.Point(0,0)
    new_list = []
    i = 0
    while i < len(list):
        new_list.append(round(euclidean_distance(list[i],origin),3))
        i += 1
    return new_list
