#!/usr/bin/env python3
from itertools import permutations
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
    def test_empty(self):
        empty = []
        self.assertEqual(_is_sorted(empty), True)
    
    def test_is_sorted(self):
        a = [5]
        self.assertEqual(_is_sorted(a), True)

        b = [0, 1]
        self.assertEqual(_is_sorted(b), True)

        c = [1, 50]
        self.assertEqual(_is_sorted(c), True)

        d = [-5, -2]
        self.assertEqual(_is_sorted(d), True)
    
    def test_is_not_sorted(self):
        e = [1, 0]
        self.assertEqual(_is_sorted(e), False)

        f = [-5, -20]
        self.assertEqual(_is_sorted(f), False)
        

class TestBogoSort(unittest.TestCase):
    def test_empty(self):
        empty = []
        self.assertEqual(bogo_sort(empty), [])
        self.assertEqual(bogo_sort_randomized(empty), [])
    
    def test_sorting(self):
        a = [5]
        self.assertEqual(bogo_sort(a), [5])
        self.assertEqual(bogo_sort_randomized(a), [5])

        b = [1, 5, 2, 42]
        self.assertEqual(bogo_sort(b), [1, 2, 5, 42])
        self.assertEqual(bogo_sort_randomized(b), [1, 2, 5, 42])

        c = [9, 8, 0, 5]
        self.assertEqual(bogo_sort(c), [0, 5, 8, 9])
        self.assertEqual(bogo_sort_randomized(c), [0, 5, 8, 9])
        
        d = [-1, -2, 0, -100]
        self.assertEqual(bogo_sort(d), [-100, -2, -1, 0])
        self.assertEqual(bogo_sort_randomized(d), [-100, -2, -1, 0])


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