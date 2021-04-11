import time

begin = time.time()
t = []


def initialize_table_calc_fib(n):
    for i in range(n + 1):
        t.append(-1)
    k = fib(n)
    end = time.time()
    print("time=", end - begin)
    print(k)


# Dynamic Approach
def fib(n):
    if n == 0 or n == 1:
        return 1
    if t[n - 1] == -1:
        t[n - 1] = fib(n - 1)
    if t[n - 2] == -1:
        t[n - 2] = fib(n - 2)
    return t[n - 1] + t[n - 2]


# Naive Approach
#
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

initialize_table_calc_fib(100)
