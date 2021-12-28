""" Day 1 Solutions """

from argparse import ArgumentParser
import sys
from collections import defaultdict, Counter
from itertools import permutations, product
import numpy as np
from aoc.y2015.utils import load_data


def ints(x):
    return list(map(int, x))


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    print("INPUT DATA:")
    # print(d)
    result_1 = d[0].count("(") - d[0].count(")")

    floor = 0
    for step, c in enumerate(d[0]):
        if c == "(":
            floor += 1
        else:
            floor += -1
        if floor == -1:
            result_2 = step + 1
            break
    return result_1, result_2


def main():
    """Main function"""
    # load data:
    print("**** REAL DATA ****")
    d = load_data("day1.txt")
    answer_1, answer_2 = solve(d)
    print("Answer 1:", answer_1)
    print("Answer 2:", answer_2)


if __name__ == "__main__":
    main()
