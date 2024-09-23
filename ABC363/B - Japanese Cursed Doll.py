N,T,P = map(int, input().split())
L = list(map(int, input().split()))
day = 0

#全探索
while True:
    t_cnt = 0
    for elm in L:
        if elm >= T:
            t_cnt+=1
    if(t_cnt >= P):
        print(day)
        exit()
    for i in range(N):
        L[i] += 1
    day+=1
    
    