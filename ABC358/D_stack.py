n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)

ans=0

while a and b:
    x=a.pop()
    y=b.pop()
    if x>=y:
        ans+=x
    else:
        b.append(y)

if b:
    print(-1)
else:
    print(ans)

