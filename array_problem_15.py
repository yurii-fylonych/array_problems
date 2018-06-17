array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]



def compare_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    c = int(input('Enter your value = '))
    counts = 0

    for item in array:
        if item == c:
            counts += 1

    return counts, None

result, error = compare_item(array)

if result == None:
    print(error)
else:
    print('We find your value {} times'.format(result))



def compare_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    c = int(input('Enter your value = '))
    counts = 0
    index = 0

    while index < len(array):
        if array[index] == c:
            counts += 1
        index += 1

    return counts, None

result, error = compare_item(array)

if result == None:
    print(error)
else:
    print('We find your value {} times'.format(result))

#Python function count

def compare_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    c = int(input('Enter your value = '))
    counts = array.count(c)

    return counts, None

result, error = compare_item(array)

if result == None:
    print(error)
else:
    print('We find your value {} times'.format(result))


def compare_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    C = int(input('Enter  value for comparison. C = '))
    count = 0

    def rec_compare(array, C, count):
        if len(array) == 0:
            return count

        if C == array[0]:
            count += 1
        return rec_compare(array[1:], C, count)

    counts = rec_compare(array, C, count)

    return counts, None


result, error = compare_item(array)

if result == None:
    print(error)
else:
    print('We find your value {} times'.format(result))