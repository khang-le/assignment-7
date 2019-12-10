#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Dec 2019
# This program uses lists and rotation


def rotation(list_of_number, ratating_time):

    numbers = list_of_number[0]
    numbers = [list_of_number[(i + ratating_time) % len(list_of_number)]
               for i, x in enumerate(list_of_number)]
    return numbers


def main():

    lst = []
    # number of elemetns as input
    user_input = int(input("Enter number of elements : "))
    rotating_time = int(input("Enter how many times you want to rotate: "))
    print("The numbers are:")
    for i in range(0, user_input):
        ele = int(input())
        lst.append(ele)  # adding the element
    numbers = rotation(lst, rotating_time)
    print("Rotated by {0}: {1}".format(rotating_time, numbers))


if __name__ == "__main__":
    main()
