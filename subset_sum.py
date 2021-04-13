def subset_sum(arr, target, n):
    if target == 0:
        return True
    if n == 0 and target != 0:
        return False
    if arr[n - 1] > target:
        return subset_sum(arr, target, n - 1)
    return subset_sum(arr, target - arr[n - 1], n - 1) or subset_sum(arr, target, n - 1)


print(subset_sum([9, 3, 5, 2], 10, 4))
