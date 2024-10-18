
N=int(input())
A=[list(input()) for _ in range(N)]
result = A[:]
result[0] = "abc"
print(A)
print(result)