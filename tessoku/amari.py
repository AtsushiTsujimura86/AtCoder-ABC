N=int(input())
codes = [None]*N
vals = [None]*N
for i in range(N):
    codes[i],vals[i] = input().split()
    vals[i] = int(vals[i])
ans = 0
for i in range(N):
    if codes[i] == "+": ans+=vals[i]
    elif codes[i] == "-": ans-=vals[i]
    else: ans*=vals[i]
    if ans<0: ans+=10000
    ans%=10000
    print(ans)