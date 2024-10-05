def find_min_difference(arr):
    total_sum = sum(arr)
    n = len(arr)
    target = total_sum // 2
    
    # DPテーブル: dp[i]は部分集合の総和がiになるかどうか
    dp = [False] * (target + 1)
    dp[0] = True  # 0の総和は常に作れる
    
    # 各要素を一つずつ見ていき、DPテーブルを更新
    for num in arr:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    # 総和の半分にできるだけ近い値を探す
    for i in range(target, -1, -1):
        if dp[i]:
            group1_sum = i
            break
    
    group2_sum = total_sum - group1_sum
    
    # より大きい方の総和を返す
    return max(group1_sum, group2_sum)

# 入力例
n=int(input())
arr=list(map(int, input().split()))
result = find_min_difference(arr)
print(result)
