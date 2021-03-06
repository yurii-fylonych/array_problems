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


def substitute_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    index = 0

    def rec_substitute_items(array, index):
        if index == len(array):
            return array
        if array[index] > 0:
            array[index] = 1
        else:
            array[index] = 0

        index += 1

        return rec_substitute_items(array, index)

    new_array = rec_substitute_items(array, index)

    return new_array, None


result, error = substitute_items(array)

if result == None:
    print(error)
else:
    print(result)

def substitute_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    count = 0
    index = 0

    def subsitute_items(array, count, index):
        if index == len(array):
            return count

        if array[index] > 7:
            array[index] = 7
            count += 1

        index += 1

        return subsitute_items(array, count, index)

    count = subsitute_items(array, count, index)

    return count, None


result, error = substitute_items(array)

if result == None:
    print(error)
else:
    print(result)

