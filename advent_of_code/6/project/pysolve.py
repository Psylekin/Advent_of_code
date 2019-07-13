import pandas as pd
import numpy as np

def connection_test():
    return 1

def create_frequencyList(shape, wayPoints):
    frequencyList = []

    closestPointList = list_closest_Points(shape, wayPoints)
    for wayPoint in wayPoints:
        frequencyList.append([wayPoint, closestPointList.count(wayPoint)])
    return frequencyList

def find_finite_areas(shape, wayPoints):
    nonInfiniteList = []
    regularList = create_frequencyList(shape, wayPoints)
    largerList = create_frequencyList(enlarge_shape(shape), wayPoints)

    for index, item in enumerate(regularList):
        if item == largerList[index]:
            nonInfiniteList.append(item)

    return nonInfiniteList


def list_closest_Points(shape, wayPoints):
    closestPointList = []

    for x in range(shape[0][0], shape[0][1]):
        for y in range(shape[1][0], shape[1][1]):
            search_for = (x,y)
            closestPointList.append(find_nearest_spot(search_for, wayPoints)[1])
    return closestPointList


def find_nearest_spot(search_for, wayPoints):
    lowScore = [10000, (0,0)]

    for spot in wayPoints:
        distance = calculate_distance(search_for, spot)
        if distance < lowScore[0]:
            lowScore[0] = distance
            lowScore[1] = spot
        elif distance == lowScore[0]:
            lowScore[1] = None
    return lowScore

def calculate_distance(startpoint, endpoint):
    distance = abs(startpoint[0] - endpoint[0]) + abs(startpoint[1] - endpoint[1])
    return distance

def enlarge_shape(shape):
    shape[0][0] += -1
    shape[0][1] += 1
    shape[1][0] += -1
    shape[1][1] += 1
    return shape

def find_highscore(finitePoints):
    highscore = [(0,0), 0]
    for listing in finitePoints:
        if highscore[1] < listing[1]:
            highscore = listing
    return highscore

def set_shape(wayPoints):
    highscoreX = 0
    highscoreY = 0

    for wayPoint in wayPoints:
        if wayPoint[0] > highscoreX:
            highscoreX = wayPoint[0]

        if wayPoint[1] > highscoreY:
            highscoreY = wayPoint[1]

    shape = [[-10, highscoreX],[-10,highscoreY]]
    return shape


with open('advent_of_code/6/project/input.txt') as input:
    wayPoints = input.read().splitlines()

for index, point in enumerate(wayPoints):
    newpoint = point.split(",")
    newpoint = int(newpoint[0]), int(newpoint[1])
    wayPoints[index] = newpoint

shape = set_shape(wayPoints)
finitePoints = find_finite_areas(shape, wayPoints)
savestPoint = find_highscore(finitePoints)
print(savestPoint[1])

#trainingWayPoints = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
