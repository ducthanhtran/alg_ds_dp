#!/usr/bin/env python3
from typing import List
import argparse
import unittest


# We restrict exchanging to the range that is still unordered.
def bubble_sort(integers: List[int]) -> List[int]:
    start = 0
    end = len(integers) - 1

    while start <= end:
        first_swap = len(integers)
        last_swap = -1

        for i in range(start, end):
            if integers[i] > integers[i+1]:
                integers[i], integers[i+1] = integers[i+1], integers[i]
                if i < first_swap:
                    first_swap = i
                last_swap = i
        
        start = max(0, first_swap - 1)
        end = last_swap
    return integers


class TestBubbleSort(unittest.TestCase):
    def test_empty(self):
        empty = []
        self.assertEqual(bubble_sort(empty), [])
    
    def test_sorting(self):
        a = [5]
        self.assertEqual(bubble_sort(a), [5])

        b = [1, 5, 2, 42]
        self.assertEqual(bubble_sort(b), [1, 2, 5, 42])

        c = [9, 8, 0, 5]
        self.assertEqual(bubble_sort(c), [0, 5, 8, 9])
        
        d = [-1, -2, 0, -100]
        self.assertEqual(bubble_sort(d), [-100, -2, -1, 0])

        e = [-1, -2, 5, 8, 5]
        self.assertEqual(bubble_sort(e), [-2, -1, 5, 5, 8])

        f = [1, 10, 20]
        self.assertEqual(bubble_sort(f), [1, 10, 20])

        g = [50, 10]
        self.assertEqual(bubble_sort(g), [10, 50])

        h = [1, 2, 3, 7, 4, 5, 6, 8, 9, 10]
        self.assertEqual(bubble_sort(h), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, nargs="+", help="Integer inputs")
    parser.add_argument('--test', action="store_true", help="Run unittest only")
    args = parser.parse_args()

    if args.test:
        unittest.main(argv=[__name__])
    else:
        print("Input: {}".format(args.i))
        print("Sorted output: {}".format(bubble_sort(args.i)))