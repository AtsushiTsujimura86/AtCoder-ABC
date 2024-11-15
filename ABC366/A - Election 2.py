N, T, A = map(int, input().split())
n_half = N//2+ 1
if T >= n_half or A >= n_half:
    print("Yes")
else: 
    print("No")