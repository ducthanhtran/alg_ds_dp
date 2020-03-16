#!/usr/bin/env python3
from typing import List
import argparse
import unittest


def insertion_sort(integers: List[int]) -> List[int]:
    for i in range(1, len(integers)):
        to_insert = integers[i]
        # Insert to_insert into already sorted integers[0], ..., integers[i-1]
        j = i - 1
        while j >= 0 and integers[j] > to_insert:
            integers[j+1] = integers[j]
            j = j - 1
        integers[j+1] = to_insert
    return integers


class TestInsertionSort(unittest.TestCase):
    def test_empty(self):
        empty = []
        self.assertEqual(insertion_sort(empty), [])
    
    def test_sorting(self):
        a = [5]
        self.assertEqual(insertion_sort(a), [5])

        b = [1, 5, 2, -9]
        self.assertEqual(insertion_sort(b), [-9, 1, 2, 5])
        
        c = [-1, -2, 0, -100]
        self.assertEqual(insertion_sort(c), [-100, -2, -1, 0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, nargs="+", help="Integer inputs")
    parser.add_argument('--test', action="store_true", help="Run unittest only")
    args = parser.parse_args()

    if args.test:
        unittest.main(argv=[__name__])
    else:
        print("Input: {}".format(args.i))
        print("Sorted output: {}".format(insertion_sort(args.i)))