array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def min_items(array):
    if len(array) <= 2:
        return None, 'Short array. Try again'

    min_item = 10000

    for index, item in enumerate(array):
        if index % 2 == 0:
            if min_item > item > 0:
                min_item = item

    return min_item, None


result, error = min_items(array)

if result == None:
    print(error)
else:
    print(result)



def min_items(array):
    if len(array) <= 2:
        return None, 'Short array. Try again'

    min_item = 10000
    index = 0

    while index < len(array):
        if index % 2 == 0:
            if min_item > array[index] > 0:
                min_item = array[index]

        index += 1

    return min_item, None


result, error = min_items(array)

if result == None:
    print(error)
else:
    print(result)


def min_items(array):
    if len(array) <= 2:
        return None, 'Short array. Try again'

    min_item = 10000

    def rec_min(array, min_item):
        if len(array) <= 2:
            return min_item
        if array[2] < min_item:
            min_item = array[2]
        return rec_min(array[2:], min_item)

    min_item = rec_min(array, min_item)

    return min_item, None


result, error = min_items(array)

if result == None:
    print(error)
else:
    print(result)
