#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 1/9/2019
    Class: CS325.400 Winter 2019
    Assignment: HW1: insertion sort
    Description: A simple Python implementation of insertion sort.
    Reads unsorted lists of integers from a file, named 'data.txt', in the current directory,
    sorts the lists and writes the sorted lists to new file, named 'insertionsort.txt'.
"""


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
    number_list = []
    with open("data.txt", "r") as ifile:  # read and parse integer lists from file.
        for line in ifile:
            data_list = []
            data = line.split()
            data.pop(0)  # remove first element, don't need it.
            for number in data:
                data_list.append(int(number))
            number_list.append(data_list)

    for x in number_list:  # sort each list.
        insertionsort(x)

    with open("insertionsort.txt", "w+") as ofile:  # write sorted lists to file.
        for x in number_list:
            for y in x:
                ofile.write("%i " % y)
            ofile.write("\n")
