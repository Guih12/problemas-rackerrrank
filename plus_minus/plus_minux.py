def plusMinus(arr, positive, negative, zero):
    for value in arr:
        if value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        elif value == 0:
            zero += 1
    
    print(float(positive) / float(len(arr)))
    print(float(negative) / float(len(arr)))
    print(float(zero) / float(len(arr)))
    
arr = [1,1,0, -1, -1]
arr2 = [-4, 3, -9, 0, 4, 1]

plusMinus(arr, 0, 0, 0)
plusMinus(arr2, 0, 0, 0)
