from math import sqrt
import random
D = 2  # dimensions


class Point:
    __coords = []
    __bool = bool()

    def __init__(self, arr, tof):
        self.__coords = arr
        __bool = tof  # tof = true of false


def euclidean_dist(D, p1, p2):
    sum = float
    for i in range(D):
        sum += pow((p2.coords[i] - p1.coords[i]), 2)
    return sqrt(sum)


def nearest_point(D, graph, val):
    min = 1000000
    for point in graph:
        dist = euclidean_dist(D, val, point)
        if dist < min:
            min = dist
            p = point
            if min == 0:
                break
    return p


def main():
    print('program running')
    # dimensions = int(input('dimensions: '))
    tof = [True, False]
    dataset = []
    for i in range(10):
        coords = []
        for j in range(D):  # x, y, z... n-dimensions
            coords.append(random.uniform(1, 50))
        dataset.append(Point(coords, tof[random.randint(0, 1)]))


main()
