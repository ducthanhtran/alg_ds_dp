#!/usr/bin/env python3
from typing import List
import argparse


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, nargs="+", help="Integer inputs")
    args = parser.parse_args()

    print("Input: {}".format(args.i))
    print("Sorted output: {}".format(insertion_sort(args.i)))