#!/usr/bin/python3
"""Define a class MyList"""


class MyList(list):
    """
    A custom list class that inherits from the build-in list class.

    Attributes:
    - No additional attributes.

    Public Methods:
    - print_sorted(): Prints the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        Args:
        - None

        Returns:
        - None
        """
        sorted_list = sorted(self)
        print(sorted_list)
