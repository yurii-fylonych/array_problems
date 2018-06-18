array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def find_2_max_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    max_el = array[0]
    sec_el = array[1]
    for item in array:
        if item > max_el:
            max_el = item

    for item in array:
        if item > sec_el and item != max_el:
            sec_el = item

    return sec_el, None


result, error = find_2_max_item(array)

if result == None:
    print(error)
else:
    print(result)


def find_2_max_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    n = len(array) - 1

    for i in range(n):
        for j in range(n - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    sec_el = array[n]

    return sec_el, None


result, error = find_2_max_item(array)

if result == None:
    print(error)
else:
    print(result)