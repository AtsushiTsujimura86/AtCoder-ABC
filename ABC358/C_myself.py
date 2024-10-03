N,M=map(int,input().split())
S=[input() for _ in range(N)]

s=[0]*N
ans = N
#ビットマスクに変換
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            s[i] |= 0b00001 << j

#すべての通りを試す
for mask in range(1 << N):
    o = 0
    for i in range(N):
        if mask >> i & 0b001:
            o |= s[i]
    if o == (0b00001 << M) -1:
        ans = min(ans, bin(mask).count("1"))
        
print(ans)