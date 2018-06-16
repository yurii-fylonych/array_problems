array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def substitution_in_array(array):
    if len(array) == 0 or len(array) == 1:
        return None, 'Short array. Try again'

    for index in array:
        if index % 2 != 0:
            array[index] = 0
    return array, None

result, array = substitution_in_array(array)

if result == None:
    print(error)
else:
    print(result)


array = [3, 5, 6, 7, 12, -4, -3, -5]


def replace_el_in_array(array):
    if len(array) == 0 or len(array) == 1:
        return None, 'Short array. Try again'

    index = 1

    while index < len(array):
        if index % 2 != 0:
            array[index] = 0
        index += 1

    return array, None


result, array = replace_el_in_array(array)

if result == None:
    print(error)
else:
    print(result)

