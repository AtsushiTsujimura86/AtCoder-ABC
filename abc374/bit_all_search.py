N=int(input())
K=list(map(int, input().split()))

diff = 10**18
k_total = sum(K)
for i in range(1 << N):
    total = 0
    k=i
    for j in range(N):
        if ((i >> j) & 1):
            print(bin(i)[2:].zfill(5), bin(j)[2:])
            total+=K[j]
        # if (k & (1 << j)):
        #     print("k",bin(k))
        #     print("1<<j", bin(1<<j))
        #     total+=K[j]
    print(total)
    diff = min(diff, max(total,k_total-total))

print(diff)
        