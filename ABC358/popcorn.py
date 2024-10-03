N,M = map(int, input().split())
S = [input() for _ in range(N)]
print(S)
s=[0]*N
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            s[i] |= 1<<j
            
for i in range(N):
    print(bin(s[i])[2:].zfill(M))
 
ans=N
for mask in range(1 << N):
    print("mask:",bin(mask)[2:].zfill(3))
    o=0
    for i in range(N):
        #iビット目が1の場合
        if mask >> i & 0b0001:
            o |= s[i]
            print("o:",bin(o)[2:].zfill(M))
    print()
    #1を左に3bitシフトして1000を作って、そこから1を引いて111を作る
    if o== (1 << M)-1:
        ans = min(ans, bin(mask).count("1"))
print(ans)