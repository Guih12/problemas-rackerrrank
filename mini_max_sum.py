def min_max_sum(arr):
    sum = 0
    min = 0

    for y in range(0, len(arr) -1 ):
        min += arr[y]

    for x in range(arr[0], len(arr)):
        sum += arr[x]

    
    print min,sum

arr = [1,3,5,7,9]
min_max_sum(arr)
min_max_sum(arr_two)

#max: 3, 5, 7, 9 remove o primeiro elemento
#min: 1,3,5,7 remove o ultimo elemento

