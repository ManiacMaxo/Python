from math import sqrt
import random
D = 2  # dimensions


class Point:
    def __init__(self, arr, tof):
        self.coords = arr
        self.bool = tof  # tof = true of false


def euclidean_dist(D, p1, p2):
    sum = 0
    for i in range(D):
        sum += (p2.coords[i] - p1.coords[i]) ** 2
    return sqrt(sum)


def distances(D, graph, new):
    dist = {}
    for i in range(len(graph)):
        dist[i] = euclidean_dist(D, graph[i], new)

    dist = sorted(dist.items(), key=lambda item: item[1])
    return dist


if __name__ == '__main__':
    print('program running')
    # dimensions = int(input('dimensions: '))
    tof = [True, False]
    dataset = []
    for _ in range(10):
        coords = []
        for _ in range(D):  # x, y, z... n-dimensions
            coords.append(random.uniform(1, 50))
        dataset.append(Point(coords, tof[random.randint(0, 1)]))
    distances(D, dataset, Point((1, 2), False))
