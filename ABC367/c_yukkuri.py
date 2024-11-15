N, K = map(int, input().split())
R = list(map(int, input().split()))

def f(i, A):
    print("i:", i)
    print("A:", A)
    if i==N:
        if sum(A) % K == 0:
            print(" ".join(map(str, A)))
    else:
        for j in range(1, R[i]+1):
            A.append(j)
            f(i+1, A)
            A.pop()
    print()

f(0, [])