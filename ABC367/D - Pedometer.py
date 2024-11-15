N, M = map(int, input().split())
A = list(map(int, input().split()))

ruiseki = [0]
for i in range(1,len(A)+1):
    ruiseki.append(A[i-1]+ruiseki[i-1])

array=[]
cnt = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            continue
        if i<j:
            if (ruiseki[j-1] - ruiseki[i-1]) % M == 0:
                cnt+=1
        else:
            if (ruiseki[-1] - (ruiseki[i-1] - ruiseki[j-1])) % M==0:
                cnt+=1
print(cnt)