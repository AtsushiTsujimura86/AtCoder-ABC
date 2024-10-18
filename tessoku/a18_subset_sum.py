N,S = map(int, input().split())
A=list(map(int, input().split()))

dp=[[None for _ in range(S+1)] for _ in range(N+1)]

dp[0][0] = 0
for i in range(1,N+1):
    for j in range(S+1):
        if dp[i-1][j] != None:
            dp[i][j] = dp[i-1][j]
        if j-A[i-1] >= 0:
            if dp[i-1][j-A[i-1]] != None:
                dp[i][j] = dp[i-1][j-A[i-1]] + A[i-1]

for i in range(N+1):
    if dp[i][-1] != None:
        print("Yes")
        exit()
print("No")
