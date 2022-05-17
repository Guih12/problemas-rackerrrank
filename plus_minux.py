def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for value in arr:
        if value > 0:
            pos += 1
        elif value < 0:
            neg += 1
        elif value == 0:
            zero += 1
    
    print(float(pos) / float(len(arr)))
    print(float(neg) / float(len(arr)))
    print(float(zero) / float(len(arr)))
    
arr = [1,1,0, -1, -1]
arr2 = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
plusMinus(arr2)
