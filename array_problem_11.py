array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]

def get_mim_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    min_el = array[0]

    for index, item in enumerate(array):
        if index % 2 != 0:
            if item < min_el:
                min_el = item

    return min_el, None


result, error = get_mim_item(array)

if error != None:
    print(error)
if error == None:
    print(result)


def get_mim_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    min_el = array[0]
    index = 0

    while index < len(array):
        if index % 2 != 0:
            if array[index] < min_el:
                min_el = array[index]
        index += 1

    return min_el, None


result, error = get_mim_item(array)

if error != None:
    print(error)
if error == None:
    print(result)



def get_mim_item(array):
    if len(array) == 0:
        return None, 'Short array. Try again'

    min_el = array[0]

    def get_min_rec(array, min_el):
        if len(array) <= 1:
            return min_el
        if array[1] < min_el:
            min_el = array[1]
            return get_min_rec(array[2:], min_el)
        else:
            return get_min_rec(array[2:], min_el)

    result = get_min_rec(array, min_el)

    return result, None


result, error = get_mim_item(array)

if error != None:
    print(error)
if error == None:
    print(result)