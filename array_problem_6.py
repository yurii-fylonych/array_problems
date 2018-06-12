array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]

def mid_number(array):
    C =int(input('Enter value C'))
    k = 0
    sum = 0

    if array == 0:
        return None, 'Enter new array. This one slightly short'

    for item in array:
        if item > C:
            k = +1
            sum += item

    if k == 0:
        return None, 'All items in array less than C'

    mid = sum / k

    return mid, None

mid, error = mid_number(array)

if error != None:
    print(error)
if error == None:
    print(mid)



def while_number(array):
    if len(array) == 0:
        return None, 'Enter new array. This array is too short'

    C = int(input('Enter value C'))
    k = 0
    sum = 0
    i = 0

    while len(array) > i:
        if C < array[i]:
            sum += array[i]
            k += 1
        i += 1

    if k == 0:
        return None, 'All elements in your array shorter than your value C'

    mid = sum / k

    return mid, None

mid_quantity, error = while_number(array)

if error != None:
    print(error)
if error == None:
    print(mid_quantity)

def main(array):
    if len(array) == 0:
        return None, 'Short array. You have infinity number of attemts'

    C = int(input('Please write quantity C'))

    def rec_number(array, C, k = 0):
        if len(array) == 0:
            return 0, k
        if C < array[0]:
            return array[0] + rec_number(array[1:], k + 1)
        else:
            return rec_number(array[1:])

    sum_numbers, quantity = rec_number(array, C, k = 0)

    return sum_numbers, quantity, None


def max_number(array):
    if len(array) == 0:
        return None, 'Short array, try again'

    C = int(input('Enter value C = '))
    k = 0
    sum = 0

    def rec_array(array, C, k):
        if len(array) == 0:
            return 0, k
        if array[0] > C:
            k += 1
            sum, k = rec_array(array[1:], C, k)
            return sum + array[0], k
        else:
            return rec_array(array[1:], C, k)

    sum, k = rec_array(array, C, k)
    aver = sum / k

    return aver, None


aver, error = max_number(array)

if error != None:
    print(error)
if error == None:
    print(aver)