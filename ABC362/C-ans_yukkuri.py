N = int(input())
L=[None]*N
R=[None]*N
for i in range(N):
    L[i], R[i] = map(int, input().split())
X = [x for x in L[i]]
s = sum(X)
T = 0
if s > T:
    print("No")
    exit()
    
for i in range(N):  
    d = min(T-s, R[i]-L[i])
    s += d
    X[i] += d

if s == T:
    print("Yes")
    print(*X)
else:
    print("No")