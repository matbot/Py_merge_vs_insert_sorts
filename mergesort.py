#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 1/9/2019
    Class: CS325.400 Winter 2019
    Assignment: HW1: merge sort
    Description: A simple Python implementation of merge sort.
    Reads unsorted lists of integers from a file, named 'data.txt', in the current directory,
    sorts the lists and writes the sorted lists to new file, named 'mergesort.txt'.
"""


# Define mergesort --based on pseudocode provided on CLRS pg.31-34.
def merge(array, start, midpoint, end):
    n1 = midpoint + 1
    left_array = array[start:n1]            # separate the subarrays to be merged.
    right_array = array[n1:end + 1]
    left_array.append(float("inf"))
    right_array.append(float("inf"))
    i = j = 0
    for k in range(start, end + 1):         # merge the partial arrays to a combined, ordered array.
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1


def mergesort(array, start, end):
    if start < end:
        midpoint = (start + end) // 2            # floor division --Python3
        mergesort(array, start, midpoint)
        mergesort(array, midpoint + 1, end)
        merge(array, start, midpoint, end)


# MAIN
if __name__ == "__main__":
    number_list = []
    with open("data.txt", "r") as ifile:  # read and parse integer lists from file.
        for line in ifile:
            data_list = []
            data = line.split()
            data.pop(0)             # remove first element, don't need it.
            for number in data:
                data_list.append(int(number))
            number_list.append(data_list)

    for x in number_list:  # sort each list.
        mergesort(x, 0, len(x) - 1)

    with open("mergesort.txt", "w+") as ofile:  # write sorted lists to file.
        for x in number_list:
            for y in x:
                ofile.write("%i " % y)
            ofile.write("\n")
