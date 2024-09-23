N = int(input())
A = list(map(int, input().split()))

zero_cnt = N
cnt = 0
A_r = sorted(A, reverse=True)
while(zero_cnt > 1):
    cnt+=1
    A_r = sorted(A_r, reverse=True)
    A_r[0] -=1
    A_r[1] -=1
    if A_r[0] <= 0:
        zero_cnt-=1
    if A_r[1] <= 0:
        zero_cnt-=1
    

print(cnt)