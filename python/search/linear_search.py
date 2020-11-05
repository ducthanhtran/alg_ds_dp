#!/usr/bin/env python3
from typing import List, Optional
import argparse
import unittest


def linear_search(integers: List[int], number: int) -> Optional[int]:
    for index, element in enumerate(integers):
        if element == number:
            return index
    return None


class Test(unittest.TestCase):
    def test_not_found(self):
        a = [-3, 5, 99]
        number = 100
        self.assertEqual(linear_search(a, number), None)

        b = []
        number = 1
        self.assertEqual(linear_search(b, number), None)
    
    def test_found(self):
        c = [5]
        number = 5
        self.assertEqual(linear_search(c, number), 0)

        d = [-1, 0, 1]
        number = -1
        self.assertEqual(linear_search(d, number), 0)

        e = [-8, 55, 0]
        number = 55
        self.assertEqual(linear_search(e, number), 1)

        f = [-8, 55, 0]
        number = 0
        self.assertEqual(linear_search(f, number), 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, nargs="+", help="Integer inputs")
    parser.add_argument('-n', type=int, help="Number to search for")
    parser.add_argument('--test', action="store_true", help="Run unittest only")
    args = parser.parse_args()

    if args.test:
        unittest.main(argv=[__name__])
    else:
        print("Input: {}".format(args.i))
        print("Searching for {}".format(args.n))
        index = linear_search(args.i, args.n)
        if index is not None:
            print("Index: {} in input list".format(index))
        else:
            print("Number not found in list of integers.")