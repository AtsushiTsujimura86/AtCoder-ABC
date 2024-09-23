n, k, x = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[:k]
A1.append(x)
A2 = A[k:]
B = A1 + A2
for i in B:
    print(i, end=" ")
