N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

dp=[10*18 for _ in range(N)]
dp[0] = 0
dp[1] = A[0]
for i in range(2,N):
    dp[i] = min(dp[i-1]+A[i-1], dp[i-2]+B[i-2])

route = [N]
val=dp[N-1]
pos=N-1
while pos != 0:
    if dp[pos]-A[pos-1] == dp[pos-1]:
        pos -=1
    else:
        pos -=2
    route.append(pos+1)
print(len(route))
print(*route[::-1])
    



    
    
