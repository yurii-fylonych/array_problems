from copy import copy
array=[1, 10, 6, 10, 12, 15]



def for_find(array):
   sum = 0
   k = 0

   if len(array) == 0:
       return input('Empty array, try again')

   for index, item in enumerate(array):
       if index % 2 != 0:
           sum += item
           k += 1

   if k == 0:
       return input('Short array, try again')

   mid = sum / k

   return mid



def while_find(array):
    sum = 0
    index = 0
    k = 0

    if len(array) == 0:
        return input('Out of order.Try again:')

    while index < len(array):
        if index % 2 != 0:
            sum += array[index]
            k += 1
        index += 1

    if k == 0:
        return input('Short array.Try again:')

    mid = sum / k

    return float(mid)


def main(array):
    if len(array) == 0:
        return input('Enter array')
    if len(array) == 1:
        return input('Short array. Try again')

    def calculate_sum(array):
        if len(array) < 2:
            return 0
        else:
            return array[1] + calculate_sum(array[2:])

    sum = calculate_sum(array)
    k = int(len(array) / 2)
    mid = sum / k

    return mid



print(main(array))

array = [1, 5, 7, 12, 3]


def main(array):
    if len(array) == 0:
        return None, 'Enter array'
    if len(array) == 1:
        return None, 'Short array. Try again'

    def calculate_sum(array):
        if len(array) < 2:
            return 0
        else:
            return array[1] + calculate_sum(array[2:])

    sum = calculate_sum(array)
    k = int(len(array) / 2)
    mid = sum / k

    return mid, None


result, error = main(array)

if error != None:
    print(error)
if error == None:
    print(result)
