N,K=map(int, input().split())
S=list(input())

result=0
cnt=0
while True:
    s=0
    e=0
    for i in range(N):
        if S[i]=="O":
            cnt+=1
            if cnt==0:
                s=i
        else:
            cnt=0
            s=0
        if cnt==K:
            result+=1
            e=i
            for j in range(s,e+1):
                S[j] = "X"
            cnt=0
    if cnt<K and i == N-1:
        break
print(result)
