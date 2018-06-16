array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def substite_zero_items(array):
    if len(array) == 0 :
        return None, 'Short array. Try again'

    if not 0 in array:
        return None, 'Zero element is absent in your list'

    for index, item in enumerate(array):
        if array[index] == 0:
            array.remove(array[index])
            array.append(0)

    return array, None


def substite_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    if not 0 in array:
        return None, 'Zero element is absent in your list'

    n = len(array)-1

    for i in range(n):
        for j in range(n - i):
            if array[j] == 0:
                array[j],array[j+1] = array[j+1], array[j]

    return array, None

result, error = substite_items(array)

if result == None:
    print(error)
else:
    print(result)


result, array = substite_zero_items(array)

if result == None:
    print(error)
else:
    print(result)


def substite_zero_items(array):
    if len(array) == 0 or len(array) == 1:
        return None, 'Short array. Try again'

    if not 0 in array:
        return None, 'Zero element is absent in your list'

    index = 0

    while index < len(array):
        if array[index] == 0:
            array.remove(array[index])
            array.append(0)

        index += 1

    return array, None


result, error = substite_zero_items(array)

if result == None:
    print(error)
else:
    print(result)

