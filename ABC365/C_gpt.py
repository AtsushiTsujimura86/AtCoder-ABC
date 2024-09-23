def max_transport_limit(N, A, M):
    # 交通費のリストAをソートする
    A.sort()

    # 二分探索の範囲を決定
    low = 0
    high = max(A)
    
    def total_subsidy(x):
        # 補助額の合計を計算する関数
        return sum(min(a, x) for a in A)
    
    while low < high:
        mid = (low + high + 1) // 2  # 上限 x の候補を計算
        if total_subsidy(mid) <= M:
            low = mid  # x が成立するなら、範囲を広げる
        else:
            high = mid - 1  # x が成立しないなら、範囲を狭める
    
    if low == max(A):
        return 'infinite'
    return low

# 使用例
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(max_transport_limit(N, A, M))  # 出力: 200
