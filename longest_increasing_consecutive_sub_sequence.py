def lengthOfLIS(nums):
    maxValue = 0
    ht = {}
    for x in nums:
        ht[x] = "T"
    print(ht)
    for x in nums:
        count = 0
        if ht[x] == 'T':
            temp = count_len(x, count, ht)
            if temp > maxValue:
                maxValue = temp
    return maxValue


def count_len(x, count, ht):
    if x not in ht:
        return 0
    if ht[x] == 'P':
        return 0
    if ht[x] == 'T':
        ht[x] = 'P'
        count = count + 1
        return 1 + count_len(x - 1, count, ht) + count_len(x+1,count,ht)


print(lengthOfLIS([0,3,2,1,8,9,3,10,11,12]))
