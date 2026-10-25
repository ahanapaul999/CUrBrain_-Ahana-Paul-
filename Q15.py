def min_absolute_value(arr):
    best = arr[0]
    min_abs = abs(arr[0])
    for num in arr[1:]:
        curr_abs = abs(num)
        if curr_abs < min_abs:
            min_abs = curr_abs
            best = num
    return best