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
