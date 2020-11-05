#!/usr/bin/env python3
from math import floor
from typing import List
import argparse
import unittest


def _slow_sort(integers: List[int], start: int, end: int) -> None:
    if start >= end:
        return
    m = floor((start + end) / 2)
    _slow_sort(integers, start, m)
    _slow_sort(integers, m+1, end)

    if integers[end] < integers[m]:
        integers[end], integers[m] = integers[m], integers[end]
    _slow_sort(integers, start, end - 1)


def do_slow_sort(integers: List[int]) -> None:
    _slow_sort(integers, 0, len(integers) - 1)


class TestSlowSort(unittest.TestCase):
    def test_empty(self):
        empty = []
        do_slow_sort(empty)
        self.assertEqual(empty, [])
    
    def test_sorting(self):
        a = [5]
        do_slow_sort(a)
        self.assertEqual(a, [5])

        b = [1, 5, 2, 42]
        do_slow_sort(b)
        self.assertEqual(b, [1, 2, 5, 42])

        c = [9, 8, 0, 5]
        do_slow_sort(c)
        self.assertEqual(c, [0, 5, 8, 9])
        
        d = [-1, -2, 0, -100]
        do_slow_sort(d)
        self.assertEqual(d, [-100, -2, -1, 0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, nargs="+", help="Integer inputs")
    parser.add_argument('--test', action="store_true", help="Run unittest only")
    args = parser.parse_args()

    if args.test:
        unittest.main(argv=[__name__])
    else:
        print("Input: {}".format(args.i))
        do_slow_sort(args.i)
        print("Sorted output: {}".format(args.i))