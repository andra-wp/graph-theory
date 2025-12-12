def LIS(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    idx = dp.index(max_len)

    lis = []
    while idx != -1:
        lis.append(arr[idx])
        idx = prev[idx]

    lis.reverse()
    return max_len, lis


arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
length, subseq = LIS(arr)

print("Panjang LIS:", length)
print("LIS:", subseq)
