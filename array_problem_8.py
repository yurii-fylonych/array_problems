array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def bubble_sort(array):
    if len(array) == 0 or len(array) == 1:
        return None, 'Short array. Try again'
    length = len(array) - 1
    for i in range(length):
        for j in range(length - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print(array)
    return array, None


result, error = bubble_sort(array)

if error != None:
    print(error)
else:
    print(result)


def bubble_sort(array):
    if len(array) == 0 or len(array) == 1:
        return None, 'Short array. Try again'

    j = 0

    length = len(array) - 1

    while j < length:
        i = 0
        while i < length:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            i += 1
        j += 1
    return array, None


result, error = bubble_sort(array)

if error != None:
    print(error)
else:
    print(result)