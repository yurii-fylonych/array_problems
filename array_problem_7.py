array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]

def for_uneven_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    for index, item in enumerate(array):
        if index % 2 != 0:
            print(item, end = ' ')

    return True, None


list_of_array, error = for_even_item(array)

if error != None:
    print(error)
if error == None:
    print(list_of_array)


def while_odd_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    index = 1

    while index < len(array):
        print(array[index])
        index += 1

    return array, None

list_of_array, error = while_even_item(array)

if error != None:
    print(error)
if error == None:
    print(list_of_array)


def main(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    def rec_func(array):
        if len(array) == 0:
            return ''
        if array[0] % 2 != 0:
            print(array[0], end=' ')
        return rec_func(array[1:])

    result = rec_func(array)

    return result, None


result, error = main(array)

if error != None:
    print(error)



