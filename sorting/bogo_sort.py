#!/usr/bin/env python3
from itertools import permutations, product
from random import shuffle
from typing import List, Sequence
import argparse
import unittest


def _is_sorted(integers: Sequence[int]) -> bool:
    if not integers:
        return True
    
    for i in range(0, len(integers) - 1):
        if integers[i] > integers[i+1]:
            return False
    return True


def bogo_sort(integers: List[int]) -> List[int]:
    for p in permutations(integers):
        if _is_sorted(p):
            return list(p)


def bogo_sort_randomized(integers: List[int]) -> List[int]:
    while not _is_sorted(integers):
        shuffle(integers)
    return integers


class TestCheckOrder(unittest.TestCase):

    def test_is_sorted(self):
        params = [
            ([], True),
            ([5], True),
            ([0, 1], True),
            ([1, 50], True),
            ([-5, -2], True),
            ([1, 0], False),
            ([3, 2, 1], False),
            ([0, -3, -1], False),
            ([-7, -20], False),
        ]
        for inp, expected_result in params:
            with self.subTest(inp=inp):
                self.assertEqual(_is_sorted(inp), expected_result)
        

class TestBogoSort(unittest.TestCase):

    def test_sorting(self):
        params = [
            ([], []),
            ([5], [5]),
            ([1, 5, 2, 42], [1, 2, 5, 42]),
            ([9, 8, 0, 5], [0, 5, 8, 9]),
            ([-1, -2, 0, -100], [-100, -2, -1, 0])
        ]
        for (unsorted, expected_result), sorter in product(params, [bogo_sort, bogo_sort_randomized]):
            with self.subTest(unsorted=unsorted, sorter=sorter):
                self.assertEqual(sorter(unsorted), expected_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, nargs="+", help="Integer inputs")
    parser.add_argument('--deterministic', action="store_true", help="Run deterministic bogo sort")
    parser.add_argument('--test', action="store_true", help="Run unittest only")
    args = parser.parse_args()

    if args.test:
        unittest.main(argv=[__name__])
    else:
        result = bogo_sort(args.i) if args.deterministic else bogo_sort_randomized(args.i)
        print("Input: {}".format(args.i))
        print("Sorted output: {}".format(result))