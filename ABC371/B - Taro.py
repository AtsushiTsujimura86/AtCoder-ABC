N,M=map(int,input().split())
A=[None]*M
B=[None]*M
for i in range(M):
    A[i],B[i] = input().split()

ieList=[True]*(N+1)
for i in range(M):
    if B[i] == "M" and ieList[int(A[i])]==True:
        print("Yes")
        ieList[int(A[i])] = None
    else:
        print("No")

