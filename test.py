s = []
N=int(input())
for i in range(N):
    n = int(input())
    while s and s[-1] < n:
        s.pop()
    s.append(n)
    print(s)