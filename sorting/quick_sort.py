#!/usr/bin/env python3
from itertools import product
from math import floor
from typing import Callable, List
import argparse
import unittest


Partitioner = Callable[[List[int], int, int], int]


def _partition_last_pivot(integers: List[int], start: int, end: int) -> int:
    pivot = integers[end]
    index = start - 1
    for j in range(start, end):
        if integers[j] <= pivot:
            index = index + 1
            integers[index], integers[j] = integers[j], integers[index]
    integers[index + 1], integers[end] = integers[end], integers[index + 1]
    return index + 1

def _quick_sort(integers: List[int], start: int, end: int, partitioner: Partitioner) -> None:
    if start < end:
        q = partitioner(integers, start, end)
        _quick_sort(integers, start, q - 1, partitioner)
        _quick_sort(integers, q + 1, end, partitioner)

def do_quick_sort(integers: List[int], partitioner: Partitioner) -> None:
    _quick_sort(integers, 0, len(integers) - 1, partitioner)


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.partitioner_selections = [_partition_last_pivot]

    def test_sorting(self):
        params = [
            ([], []),
            ([1], [1]),
            ([0], [0]),
            ([1, 5, 2, 42], [1, 2, 5, 42]),
            ([-1, -2, 0, -100], [-100, -2, -1, 0]),
            ([-3, -0.22, -5, -1], [-5, -3, -1, -0.22]),
        ]
        for partitioner in self.partitioner_selections:
            for unsorted, expected_result in params:
                with self.subTest(unsorted=unsorted, partitioner=partitioner):
                    do_quick_sort(unsorted, partitioner)
                    self.assertEqual(unsorted, expected_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, nargs="+", help="Integer inputs")
    parser.add_argument('--test', action="store_true", help="Run unittest only")
    args = parser.parse_args()

    if args.test:
        unittest.main(argv=[__name__])
    else:
        print("Input: {}".format(args.i))
        do_quick_sort(args.i)
        print("Sorted output: {}".format(args.i))