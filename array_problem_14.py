array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def has_equal_items(array):
    if len(array) <= 1:
        return None, 'Short array. Try again'

    set_array = set(array)
    check_array = list(set_array)

    if len(array) == len(check_array):
        return 'Your array contains only unique items', None
    else:
        return 'Your array includes similar elements', None


result, error = has_equal_items(array)

if result == None:
    print(error)
else:
    print(result)

