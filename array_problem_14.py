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


def has_equal_items(array):
    if len(array) <= 1:
        return None, 'Short array. Try again'

    condition = False
    n = len(array)

    for i in range(n):
        for j in range(1 + i, n - 1):
            if array[i] == array[j]:
                condition = True

    return condition, None


result, error = has_equal_items(array)

if result == None:
    print(error)
elif result == True:
    print('Your array includes similar elements')
else:
    print('Your array contains only unique items')

# In previously sorted array
def has_equal_items(array):
    if len(array) <= 1:
        return None, 'Short array. Try again'

    n = len(array) - 1
    condition = False
    array.sort()
    index = 0

    while index < n:
        if array[index] == array[index + 1]:
            condition = True

        index += 1

    return condition, None


result, error = has_equal_items(array)

if result == None:
    print(error)
elif result == True:
    print('Your array includes similar elements')
else:
    print('Your array contains only unique items')
