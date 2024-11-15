N=int(input())
Q=[0 for _ in range(N)]
R=[0 for _ in range(N)]
for i in range(N):
    Q[i], R[i] = map(int, input().split())
Que=int(input())
T=[0 for _ in range(Que)]
D=[0 for _ in range(Que)]
for i in range(Que):
    T[i], D[i] = map(int, input().split())
    
def next_multiple_of_7_with_remainder_3(n,q,r):
    # nよりも大きい最小の7で割って3余る数を探す
    next_num = (n // q) * q + r
    if next_num < n:
        next_num += q
    return next_num
for i in range(Que):
    t = T[i] #種類
    d = D[i] #日付
    print(next_multiple_of_7_with_remainder_3(d, Q[t-1], R[t-1]))
    # if d%Q[t-1] == R[t-1]:
    #     print(d)
    # else:
        
    #     print(((d//7)+1)*7+3)
        
    
    