from copy import copy

array=[1, 10, 3, 10, 3, 15, 3, 4, -3]


def for_sum(array):
    sum = 0

    for index, item in enumerate(array):
        if index % 2 == 0:
            sum += item

    return sum




def while_sum(array):
    sum = 0
    index = 0

    if len(array) == 0:
        return None, 'Please, Try Again. Your array is too short'

    while len(array) > index:
        sum += array[index]
        index += 2

    return sum, None

sum, error = while_sum(array)

if error != None:
    print(error)
if error is None:
    print(sum)

