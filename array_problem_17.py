array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]



def has_negative_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    count = 0

    for item in array:
        if item < 0:
            count += 1

    return count, None


result, error = has_negative_items(array)

if result == None:
    print(error)
else:
    print('Array has {} negative elements'.format(result))



def has_negative_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    count = 0
    index = 0

    while index < len(array):
        if array[index] < 0:
            count += 1

        index += 1

    return count, None


result, error = has_negative_items(array)

if result == None:
    print(error)
else:
    print('Array has {} negative elements'.format(result))


def count_negative_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    count = 0
    index = 0

    def rec_has(array, count):
        if len(array) == 0:
            return count

        if array[0] < 0:
            count += 1

        return rec_has(array[1:], count)

    count = rec_has(array, count)

    return count, None


result, error = count_negative_items(array)

if result == None:
    print(error)
else:
    print('Array has {} negative elements'.format(result))

