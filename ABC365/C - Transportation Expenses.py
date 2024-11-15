N, M = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = M
x = M//2
while x < right:
    hojo_sum = 0
    for j in range(N):
        if hojo_sum >= 0:
            hojo_sum += min(x, A[j])
            
    #二分探査    
    if hojo_sum >= 0:
        left = x
    else:
        right = x
    x = (left + right)//2
    print(x)
print(x)
                   