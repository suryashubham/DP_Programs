t = [[], []]

# naive approach
# def knapsack(wt, val, capacity, n):
#     if n == 0 or capacity == 0:
#         return 0
#     if wt[n - 1] <= capacity:
#         return max(val[n - 1] + knapsack(wt, val, capacity - wt[n - 1], n - 1), knapsack(wt, val, capacity, n - 1))
#     if wt[n - 1] > capacity:
#         return knapsack(wt, val, capacity, n - 1)

# memoization approach
def knapsack(wt, val, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if t[n][capacity] != -1:
        return t[n][capacity]
    if wt[n - 1] <= capacity:
        t[n][capacity] = max(val[n - 1] + knapsack(wt, val, capacity - wt[n - 1], n - 1),
                             knapsack(wt, val, capacity, n - 1))
        return t[n][capacity]
    if wt[n - 1] > capacity:
        t[n][capacity] = knapsack(wt, val, capacity, n - 1)
        return t[n][capacity]

# could be improvised by taking dynamic inputs
def ks(n, w):
    global t
    t = [[-1 for i in range(w + 4)] for j in range(n + 4)]
    print(knapsack([30, 20, 10], [120, 100, 60], 50, 3))
