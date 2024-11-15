#動的計画法、二次元配列、しゃくとり法
#N枚のカードにそれぞれ数字が書かれていて、ある数Kを作ることができるかどうかを判定

# N, K = map(int, input().split())
# cards = list(map(int, input()))
N=3
K=7
cards = [2,2,3]
dp=[[None]*(K+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1,N+1):
    for j in range(0, K+1):
        if dp[i-1][j] == True:
            dp[i][j] = True
        elif dp[i-1][j-cards[i-1]] == True:
            print(i-1,j-cards[i-1])
            dp[i][j] = True
        else:
            continue

print(dp)
print(dp[N][K])