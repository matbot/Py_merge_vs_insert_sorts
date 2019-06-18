#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 1/9/2019
    Class: CS325.400 Winter 2019
    Assignment: HW1: insertion sort --timed.
    Description: A simple Python implementation of insertion sort.
    Times the execution of the sort on arrays of random integers of increasing size and prints
        the results to the terminal.
"""
from random import randint
from timeit import timeit

# Define insertionsort --based on pseudocode provided on CLRS pg.26.
def insertionsort(array):
    for i in range(1, len(array)):
        index = i - 1
        value = array[i]
        while index >= 0 and array[index] > value:  # shift sorted values right until index value finds correct place.
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = value


# MAIN
if __name__ == "__main__":
    for x in range(0, 30001, 3000):
        rand_ints = []
        for y in range(x):
            rand_ints.append(randint(0, 10000))
        time = timeit(lambda: insertionsort(rand_ints.copy()), number=10)
        print("n: %i  time: %f seconds" % (x, time))

