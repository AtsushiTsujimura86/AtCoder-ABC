import numpy as np
M=int(input())
t=np.base_repr(M,3)
print(t)
t=t[::-1]
print(t)
result = [int(x) for x in t]
print(len(result))
print(*result)

M=int(input())
result=[]
# while M>0:
#     a=0
#     while 3**(a+1) <=M:
#         a+=1
#     result.appned(a)
#     M-=3**a

def calc(n):
    print(n)
    if n == 0:
        return
    cnt=0
    while (3**cnt) <= n:
        cnt+=1
    result.append(cnt-1)
    return calc(n-(3**(cnt-1)))
calc(M)
print(len(result))
print(*result)

