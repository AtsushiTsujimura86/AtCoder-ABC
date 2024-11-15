N=int(input())
A=list(map(int, input().split()))
B=[0 for _ in range(N)]
dict = {}
for i in range(N):
    if str(A[i]) in dict:
        B[i] = dict.get(str(A[i])) 
        dict[str(A[i])] = i+1
    else:
        B[i] = -1
        dict[str(A[i])] = i+1
print(*B)