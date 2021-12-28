""" Day 3 Solutions """

from argparse import ArgumentParser
from collections import defaultdict
import os
from aocd import submit
from aoc.y2015.utils import load_data


def ints(x):
    return list(map(int, x))


MOVE = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    loc = (0, 0)
    visits = set()
    visits.add(loc)
    for step in d[0]:
        move = MOVE[step]
        loc = loc[0] + move[0], loc[1] + move[1]
        visits.add(loc)

    result_1 = len(visits)

    visits = set()
    visits.add((0, 0))
    loc1 = (0, 0)
    loc2 = (0, 0)
    turn = True
    for step in d[0]:
        move = MOVE[step]
        if turn:
            loc1 = loc1[0] + move[0], loc1[1] + move[1]
            visits.add(loc1)
        else:
            loc2 = loc2[0] + move[0], loc2[1] + move[1]
            visits.add(loc2)
        turn = not turn

    result_2 = len(visits)

    return result_1, result_2


def main():
    """Main function"""
    args = ArgumentParser()
    args.add_argument("--skip", action="store_true")
    args.add_argument("--submit", type=int)
    args = args.parse_args()
    # load data:
    if not args.skip:
        print("Running Tests")
        assert solve(["^v"]) == (2, 3)
        assert solve(["^>v<"]) == (4, 3)
        assert solve(["^v^v^v^v^v"]) == (2, 11)
    print("**** REAL DATA ****")
    d = load_data("day3.txt")
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
