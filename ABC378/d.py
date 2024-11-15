H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
# すでに訪れたマスを記録する配列
visited = [[False] * W for _ in range(H)]

def dfs(i,j,k):
    global ans
    print(f"ans= {ans}")
    if k==K:
        ans+=1
        return
    visited[i][j] = True
    for di, dj in [(1,0), (0,1),(-1,0), (0,-1)]:
        ni,nj=i+di,j+dj
        if 0<=ni<H and 0<=nj<W and S[ni][nj] == "." and not visited[ni][nj]:
            dfs(ni,nj,k+1)
            
    visited[i][j] = False
    
    
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            dfs(i,j,0)
print(ans)

    