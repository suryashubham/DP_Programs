t = [[], []]


def subset_sum(arr, target, n):
    if target == 0:
        return True
    if n == 0 and target != 0:
        return False
    if t[n][target] != -1:
        return t[n][target]
    if arr[n - 1] > target:
        t[n][target] = subset_sum(arr, target, n - 1)
        return t[n][target]
    t[n][target] = subset_sum(arr, target - arr[n - 1], n - 1) or subset_sum(arr, target, n - 1)
    return t[n][target]


def ss(n, s):
    global t
    t = [[-1 for i in range(s + 2)] for j in range(n + 2)]
    print(subset_sum([9, 3, 5, 2], 4, 4))
