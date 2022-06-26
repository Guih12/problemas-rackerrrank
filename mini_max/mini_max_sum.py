def min_max(arr):
    sum = 0
    for x in range(arr[0], len(arr)):
        sum += arr[x]

    return sum

def min_min(arr):
    min = 0
    for y in range(0, len(arr) -1 ):
        min += arr[y]
    
    return min

arr = [1,3,5,7,9]

#max: 3, 5, 7, 9 remove o primeiro elemento
#min: 1,3,5,7 remove o ultimo elemento

