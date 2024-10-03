N,M=map(int, input().split())
U=[None]*M
V=[None]*M
W=[None]*M
G=[[] for _ in range(N+1)]
for i in range(N):
    U[i], V[i], W[i] = map(int, input().split())

for i in range(N):
    G[U[i]].append(V[i])

G_n = [None]*(N+1)
G_n[1] = 0
for i in range()
for j in range(1,N+1):
    