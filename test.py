N=int(input())
K=list(map(int, input().split()))
k_total=sum(K)
ans = 10**18

for i in range(1<<N):
    total=0
    for j in range(N):
        if (i>>j)&1:
            total+=K[j]
    ans=min(ans, max(total, k_total-total))
    
print(ans)
print()