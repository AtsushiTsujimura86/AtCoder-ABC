N, A, B = map(int,input().split())
isWin=[None]*(N+1)

for i in range(1,N+1):
    if i < A and i < B:
        continue
    if isWin[i-A]  == None:
        isWin[i] = True
    if isWin[i-B] == None:
        isWin[i] = True
    
print(isWin)