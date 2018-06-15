array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def array_with_even_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    B = []

    for index, item in enumerate(array):
        if index % 2 != 0:
            B.append(item)

    return B, None


result, error = array_with_even_items(array)

if error != None:
    print(error)
else:
    print(result)




def array_with_even_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    B = []
    index = 0

    while index < len(array):
        if index % 2 != 0:
            B.append(array[index])
        index += 1

    return B, None


result, error = array_with_even_items(array)

if error != None:
    print(error)
else:
    print(result)



def array_with_even_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    B = []

    def rec_array(array, B):
        if len(array) == 0 or len(array) == 1:
            return B

        B.append(array[1])
        return rec_array(array[1:], B)

    result = rec_array(array, B)

    return result, None


result, error = array_with_even_items(array)

if error != None:
    print(error)
else:
    print(result)