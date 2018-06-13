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


