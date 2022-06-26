def birthdayCakeCandles(candles):
    value_max = max(candles)
    count = 0
    for i in range(len(candles)):
        if candles[i] == value_max:
            count = count + 1
    return count
##time complexity solve: O(n)