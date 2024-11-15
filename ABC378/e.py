# 入力の受け取り
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の計算
SA = [0] * N
SA[0] = A[0]
for i in range(1, N):
    SA[i] = SA[i - 1] + A[i]

# 部分和のモジュロ計算と総和
total_sum = 0
for i in range(N):
    for j in range(i, N):
        # SA[j] - SA[i-1] は A[i] + A[i+1] + ... + A[j] の和
        if i == 0:
            partial_sum = SA[j]  # 累積和そのまま
        else:
            partial_sum = SA[j] - SA[i - 1]
        
        # モジュロ演算をして合計
        total_sum += partial_sum % M

print(total_sum)
