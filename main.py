#!/bin/python

import argparse
import matplotlib.pyplot as plt
from pprint import pprint
from point_generator import generate_points
from lib import min_convex_closure


parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Test project")
parser.add_argument("-p", "--points", type=int, default=228, dest="points_number", help="Number of points in sample")
parser.add_argument("-r", "--range", nargs=2, type=int, default=[-228, 228], dest="range", help="Number of points in sample")
parser.add_argument("-v", "--visualize", action="store_true", dest="vis", help="Visialize steps")


if __name__ == '__main__':
    args = parser.parse_args()

    X, Y = generate_points(args.points_number, args.range)
    points = list(zip(X, Y))
    print(min_convex_closure(points))

    if args.vis:
        plt.scatter(X, Y)
        plt.show()
