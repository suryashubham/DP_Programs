import time

t = [list, list]
begin = time.time()


# Brute force/naive approach
# def calculate_total_no_of_paths_in_grid(m, n):
#     if m == 1 or n == 1:
#         return 1
#     return calculate_total_no_of_paths_in_grid(m - 1, n) + calculate_total_no_of_paths_in_grid(m, n - 1)

def paths(m, n):
    initialize_table(m, n)
    k = calculate_total_no_of_paths_in_grid(m, n)
    end = time.time()
    print(k)
    print("time:", end - begin)


# DP approach
def calculate_total_no_of_paths_in_grid(m, n):
    if m == 1 or n == 1:
        return 1
    if t[m - 1][n] == -1:
        t[m - 1][n] = calculate_total_no_of_paths_in_grid(m - 1, n)
    if t[m][n - 1] == -1:
        t[m][n - 1] = calculate_total_no_of_paths_in_grid(m, n - 1)

    return t[m - 1][n] + t[m][n - 1]


def initialize_table(m, n):
    global t
    t = [[-1 for i in range(m + 1)] for j in range(n + 1)]


print(paths(200, 200))
