from copy import copy

array = [1, 5, 6, 10, -13, 7, 3, 5]


def for_mult(array,y=1):

    for item in array:
        if item % 3 == 0:
            y*=item
    return y


def for_mult2(array):
    mult = 1

    if len(array) == 0:
        return input('Enter new array')

    for item in array:
        if item % 3 == 0:
           mult *= item
    if mult == 1:
        return print('Absent values aliquot to 3')

    return mult




def while_mult(array):
    mult = 1
    k = 0

    if len(array) == 0:
        return input('Enter new array')

    while k < len(array):
        if array[k] % 3 == 0:
            mult *= array[k]
        k += 1

    if mult == 1:
        return print('Absent values aliquot to 3')

    return mult


def main(array):
    if len(array) == 0:
        return ('Empty array')

    def rec_mult(array):

        if len(array) == 0:
            return 1

        for item in array:
            if item % 3 == 0:
                return int(item) * (rec_mult(array[1:]))
            else:
                return rec_mult(array[1:])

    mult = rec_mult(array)

    if mult == 1:
        return print('Absent values aliquot to 3')

    return mult


print(main(array))
