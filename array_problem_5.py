from copy import copy


array = [1, 10, 3, 10, 3, 15, 3, 4, -3]
array = [10, 3, 16, 99, 22, 100, 44, 22, -12, 33, 21]


def max_number(array):
    if len(array) == 0:
        return None, 'Short array, try again'

    index = 0
    max_num = array[0]

    for i, item in enumerate(array):
        if item > max_num:
            max_num = item
            index = i

    result = dict([('index', index), ('max_num', max_num)])

    return result, None


result, error = max_number(array)

if error != None:
   print(error)
if error == None:
   print('Max number in your array is {}, his number is {}!'.format(result['index'], result['max_num']))

