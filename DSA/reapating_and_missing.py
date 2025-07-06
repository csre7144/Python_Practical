def find_missing_and_repeating(arr):
    n = len(arr)
    total_sum = n * (n + 1) // 2
    total_sq_sum = n * (n + 1) * (2 * n + 1) // 6

    actual_sum = sum(arr)
    actual_sq_sum = sum(x * x for x in arr)

    diff = total_sum - actual_sum          
    sq_diff = total_sq_sum - actual_sq_sum 

    sum_val = sq_diff // diff

    missing = (diff + sum_val) // 2
    repeating = missing - diff

    return (repeating, missing)

arr = [4, 3, 6, 2, 1, 1]
print(find_missing_and_repeating(arr))