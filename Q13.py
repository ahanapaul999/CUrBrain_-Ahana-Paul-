def check_divisible_prefix_subarray(arr, k):
    if not arr:
        return False
    k = abs(k)
    running_sum = 0
    for num in arr:
        running_sum += num
        if running_sum % k == 0:
            return True
    return False