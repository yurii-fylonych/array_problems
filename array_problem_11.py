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

