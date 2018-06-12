from copy import copy

array=[1, 10, 3, 10, 3, 15, 3, 4, -3]


def for_sum(array):
    sum = 0

    for index, item in enumerate(array):
        if index % 2 == 0:
            sum += item

    return sum

