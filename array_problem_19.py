array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def substitute_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    for index, item in enumerate(array):
        if item > 0:
            array[index] = 1
        else:
            array[index] = 0

    return array, None


result, error = substitute_items(array)

if result == None:
    print(error)
else:
    print(result)


def substitute_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    index = 0

    while index < len(array):
        if array[index] > 0:
            array[index] = 1
        else:
            array[index] = 0
        index += 1

    return array, None


result, error = substitute_items(array)

if result == None:
    print(error)
else:
    print(result)



