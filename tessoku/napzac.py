N=4
W=7
W_item = [3,3,5,1]
V_item = [13,17,29,10]

dp=[[-10**3]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    for j in range(W+1):
        print(f"i{i}, j{j}")
        if j<W_item[i-1]:
            dp[i][j] = dp[i-1][j]            
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W_item[i-1]]+V_item[i-1])
print(dp)
print(max(max(dp)))

#-987とかになってるのは仕方ない