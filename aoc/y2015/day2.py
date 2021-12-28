""" Day 2 Solutions """

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
    print(d)
    total = 0
    ribbon = 0
    for row in d:
        dims = ints(row.split("x"))
        from itertools import product

        dims = sorted(dims)
        total += 2 * (dims[0] * dims[1] + dims[1] * dims[2] + dims[0] * dims[2])
        total += dims[0] * dims[1]
        ribbon += np.prod(dims) + 2 * (dims[0] + dims[1])

    result_1 = total
    result_2 = ribbon

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
        d = load_data("test_day2.txt")
        test_answer_1 = 0
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
    d = load_data("day2.txt")
    answer_1, answer_2 = solve(d)
    print("Answer 1:", answer_1)
    print("Answer 2:", answer_2)
    if args.submit == 1:
        from aocd import submit

        submit(answer_1, part="a", day=2, year=2015)
    if args.submit == 2:
        from aocd import submit

        submit(answer_2, part="b", day=2, year=2015)


if __name__ == "__main__":
    main()
