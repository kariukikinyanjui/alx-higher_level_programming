#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_values = set()
    total_sum = 0

    for num in my_list:
        if num not in uniq_values:
            total_sum += num
            uniq_values.add(num)

    return total_sum
