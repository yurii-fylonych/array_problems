array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]

def array_with_even_items(array):
    if len(array) == 0 or len(array) == 1:
        return None, 'Short array. Try again'

    B = []

    for item in array:
        if item % 2 == 0:
            B.append(item)

    return B, None


result, error = array_with_even_items(array)

if error != None:
    print(error)
else:
    print(result)


def array_with_even_items(array):
    if len(array) == 0 or len(array) == 1:
        return None, 'Short array. Try again'

    B = []
    i = 0

    while i < len(array):
        if array[i] % 2 == 0:
            B.append(array[i])
        i += 1

    return B, None


result, error = array_with_even_items(array)

if error != None:
    print(error)
else:
    print(result)


