N,M=map(int, input().split())
X=list(map(int, input().split()))
A=list(map(int, input().split()))

if sum(A) != N:
    print(-1)
    exit()


if 1 not in X:
    print(-1)
    exit()

result=0
for i in range(M):
    #右端の処理
    if i==M-1:
        between = N - X[i]
    else:
        between = X[i+1] - X[i]-1
    if A[i] == between+1:
        result+= between*(between+1)//2
    elif A[i] > between+1:
        result+= between*(between+1)//2
        #残りの石を次の石のあるマス（最初から石があるマス）に移動させる
        if i!=M-1:
            A[i+1] += A[i]-between-1
        result+=(between+1)*(A[i]-between-1)
    else:
        print(-1)
        exit()

print(result)


        
    