def get_shortest_path(matrix,row:int,col:int)-> int:
    dp = [[0]*row for _ in range(col)]

    #fill first row
    for i in range(row):
        dp[i][0] = matrix[0][0] if i==0 else dp[i-1][0]+matrix[i][0]
    #print(dp)

    #fill first col
    for j in range(col):
        dp[0][j] = matrix[0][0] if j == 0 else dp[0][j - 1] + matrix[0][j]
    #print(dp)

    #iterate over left-over matrix
    for k in range(1,col):
        for p in range(1,row):
            dp[k][p] = matrix[k][p] + min(dp[k-1][p],dp[k][p-1])
    return dp[row-1][col-1]


mat = [
    [1,3,3],
    [4,2,1],
    [1,1,1]
]

print(get_shortest_path(mat,3,3))
