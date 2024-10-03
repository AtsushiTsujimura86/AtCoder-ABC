S=input()
N=len(S)
pos=[0]*N
for i in range(N):
    print(i, ord(S[i]))
    pos[ord(S[i]) - ord("A")] = i
print(pos)
ans = 0
for i in range(N-1):
    ans += abs(pos[i+1] - pos[i])
print(ans)