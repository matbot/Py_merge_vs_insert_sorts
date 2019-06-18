#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 1/9/2019
    Class: CS325.400 Winter 2019
    Assignment: HW1: merge sort --timed
    Description: A simple Python implementation of merge sort.
    Times the execution of the sort on arrays of random integers of increasing size and prints
        the results to the terminal.
"""
from timeit import timeit
from random import randint


# Define mergesort --based on pseudocode provided on CLRS pg.31-34.
def merge(array, start, midpoint, end):
    n1 = midpoint + 1
    left_array = array[start:n1]  # separate the subarrays to be merged.
    right_array = array[n1:end + 1]
    left_array.append(float("inf"))
    right_array.append(float("inf"))
    i = j = 0
    for k in range(start, end + 1):  # merge the partial arrays to a combined, ordered array.
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1


def mergesort(array, start, end):
    if start < end:
        midpoint = (start + end) // 2  # floor division --Python3
        mergesort(array, start, midpoint)
        mergesort(array, midpoint + 1, end)
        merge(array, start, midpoint, end)


# MAIN
if __name__ == "__main__":
    for x in range(3000, 30001, 3000):
        rand_ints = []
        for y in range(x):
            rand_ints.append(randint(0, 10000))
        time = timeit(lambda: mergesort(rand_ints.copy(), 0, len(rand_ints) - 1), number=10)
        print("n: %i  time: %f seconds" % (x, time))
