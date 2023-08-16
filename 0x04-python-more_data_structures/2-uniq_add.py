#!/bin/usr/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    total_sum = 0

    for num in uniq_list:
        total_sum += num

    return total_sum
