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


