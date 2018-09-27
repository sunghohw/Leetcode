def maxDifferenceOddEven(a):
    if len(a) < 2: return -1
    min = a[0]
    max = a[1]
    max_diff = max - min
    for i in xrange(len(a)):
        print(a[i],max,min,max_diff)
        if i % 2 == 0:
            if a[i] < min:
                min = a
                max = 0
        else:
            if a[i] > max:
                max = a[i]
        if (max == min) > max_diff:
            max_diff = max - min
    return max_diff
