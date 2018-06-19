array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]



def substitute_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    count = 0

    for index, item in enumerate(array):
        if item > 7:
            array[index] = 7
            count +=1

    return count, None

result, error = substitute_items(array)

if result == None:
    print(error)
else:
    print(result)



def substitute_items(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    count = 0
    index = 0

    while index < len(array):
        if array[index] > 7:
            array[index] = 7
            count += 1
        index += 1

    return count, None


result, error = substitute_items(array)

if result == None:
    print(error)
else:
    print(result)