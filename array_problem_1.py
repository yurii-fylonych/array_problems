from copy import copy

array=[1, 5, -7, 10, -13]



def sum(array,y=0):
    for item in array:
        y+=int(item)
    return y


def sum_while(array):
    s=0
    y=0
    while s<len(array)>1:
        y+=int(array[s])
        s+=1
    return y


sum_while(array)

def sum_rec(array):
    ar = copy(array)
    if len(ar)==0:
        return 0
    else:
        k = ar.pop()
        return k+sum_rec(ar)



def sum_rec2(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_rec(array[1:])



print(sum_rec2(array))