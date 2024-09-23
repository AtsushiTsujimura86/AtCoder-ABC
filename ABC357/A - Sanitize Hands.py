N,M = map(int, input().split())
H = list(map(int, input().split()))

for i in range(N):
    M -=H[i]
    if M<0:
        i-=1
        break
print(i+1)