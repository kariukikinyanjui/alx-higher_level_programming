#!/bin/usr/python3
def uniq_add(my_list=[]):
    unique_values = set()
    total_sum = 0

    for num in my_list:
        if num not in unique_values:
            total_sum += num
            unique_values.add(num)

    return total_sum
