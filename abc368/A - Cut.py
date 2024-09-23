N, K = map(int, input().split())
A = list(map(int, input().split()))
# print(A[-K:])
# print(A[:N-K])
A = A[-K:]+A[:N-K]
print(" ".join(map(str, A)))