#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using a binary search_based
    approach.

    Args:
    - list_of_integers (list): The list of unsorted integers.

    Returns:
    - int or None: The peak element if found, None otherwise.

    Note:
    - A peak element is an element that is greater than or equal to its
    neighbors.

    Complexity:
    - Time: O(long(n)) where n is the length of the input list.
    - Space: O(1) (constant space usage)
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return (list_of_integers[left])
