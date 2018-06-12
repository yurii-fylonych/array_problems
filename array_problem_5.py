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


def while_max(array):
    i = 0
    maxx = array[0]
    index = i

    if len(array) == 0:
        return None, 'Enter new array'

    while len(array) > i:
        if maxx < array[i]:
            maxx = array[i]
            index = i

        i += 1

    result = {'maxx': maxx, 'index': index
              }

    return result, None


result, error = while_max(array)

if error != None:
    print(error)
if error == None:
    print('Max number in your array is {}, his number is {}!'.format(result['maxx'], result['index']))


def main(array):
    if len(array) == 0:
        return None, None, 'Short array. Try again'

    maxx = array[0]

    def find_max(array):
        if len(array) == 1:
            return array[0]

        if array[0] >= array[1]:
            array[0], array[1] = array[1], array[0]
            return find_max(array[1:])
        else:
            return find_max(array[1:])

    max_number = find_max(array)
    index = array.index(max_number)

    return max_number, index, None


max_number, index, error = main(array)

if error != None:
    print('Bro, something wrong')
else:
    print('We have done it!.Max number in your array is {}, his number is {}!'.format(max_number, index))


