def min_sum_partition(nums):
    total_sum = sum(nums)
    n = len(nums)
    half_sum = total_sum // 2

    dp = [False] * (half_sum + 1)
    dp[0] = True

    for num in nums:
        for j in range(half_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    for j in range(half_sum, -1, -1):
        if dp[j]:
            return max(j, total_sum - j)

# Test the function with the provided list
n=int(input())
result = min_sum_partition(list(map(int, input().split())))
print(result)