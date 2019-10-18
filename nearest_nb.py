from math import sqrt
D = 2  # dimensions


class Point:
    __coords = []

    def __init__(self, D, arr):
        self.__coords = arr


def euclidean_dist(D, p1, p2):
    sum = float
    for i in range(D):
        sum += p1.coords[i] + p2.coords[i]
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
    graph = []
    val = Point(D, (20, 1))
    nearest_point(2, graph, val)


main()
