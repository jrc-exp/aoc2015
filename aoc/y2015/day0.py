""" Day 0 Solutions """

from argparse import ArgumentParser
import os
import sys
from collections import defaultdict, Counter
from itertools import permutations, product
from aocd import submit
import numpy as np
from aoc.y2015.utils import load_data


def ints(x):
    return list(map(int, x))


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    print("INPUT DATA:")
    print(d)
    return result_1, result_2


def main():
    """Main function"""
    args = ArgumentParser()
    args.add_argument("--skip", action="store_true")
    args.add_argument("--submit", type=int)
    args = args.parse_args()
    # load data:
    if not args.skip:
        print("**** TEST DATA ****")
        d = load_data("test_day0.txt")
        test_answer_1 = TEST_ANSWER
        test_answer_2 = 0
        test_solution_1, test_solution_2 = solve(d)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    d = load_data("day0.txt")
    answer_1, answer_2 = solve(d)
    print("Answer 1:", answer_1)
    print("Answer 2:", answer_2)
    if args.submit == 1:
        day = int(os.path.basename(__file__).split(".")[0][3:])
        submit(answer_1, part="a", day=day, year=2015)
    if args.submit == 2:
        day = int(os.path.basename(__file__).split(".")[0][3:])
        submit(answer_2, part="b", day=day, year=2015)


if __name__ == "__main__":
    main()
