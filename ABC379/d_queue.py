import sys
input = lambda :sys.stdin.readline()[:-1]
ni = lambda :int(input())
na = lambda :list(map(int,input().split()))
yes = lambda :print("yes");Yes = lambda :print("Yes");YES = lambda : print("YES")
no = lambda :print("no");No = lambda :print("No");NO = lambda : print("NO")
#######################################################################
q = ni()

T = 0
from collections import deque
dq = deque()

for i in range(q):
    que = na()
    if que[0] == 1:
        dq.append(T)
    elif que[0] == 2:
        T += que[1]
    else:
        cnt = 0
        while dq and T - dq[0] >= que[1]:
            dq.popleft()
            cnt += 1
        print(cnt)
