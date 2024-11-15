N,A=map(int,input().split())
T = list(map(int,input().split()))

pre=0
for t in T:
    u=max(pre,t) + A
    print(u)
    pre=u