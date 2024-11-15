N,M=map(int, input().split())
g=[[] for _ in range(N)]
for _ in range(M):
    u,v,w = map(int, input().split())
    u,v = u-1, v-1
    g[u].append((v,w))
    g[v].append((u,-w))

INF=10**18
x=[INF]*N

def dfs(u):
    for v,w in g[u]:
        if x[v] == INF:
            x[v] = x[u] + w
            dfs(v)

for i in range(N):
    if x[i] == INF:
        x[i] = 0
        dfs(i)
print(*x)