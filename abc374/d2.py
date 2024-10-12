"""
<方針>
- それぞれの線分をどの順番で印字するか`O(N!)`．
- それぞれの線分をどちら(`AB` or `CD`)から印字するか`O(2^N)`．
- 毎回線分を足し合わせる操作`O(N)`．
- `N==6` なので，`O(N! * 2^N * N) <= 276480` より十分間に合いそう．
"""

import itertools
N,S,T = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(N)]

def makeDistance(y,x,Y,X):
    return ((y-Y)**2 + (x-X)**2)**0.5

ans=10**18
#どの順番で線分をたどっていくか
for seq in itertools.permutations(range(N)):
    print(seq)
    #どちらから印字するか、bit全探索
    for i in range(1 << N):
        tmp = 0 # 現在の距離
        y = 0 # 現在の位置
        x = 0 # 現在の位置
        for j in range(N):
            A,B,C,D = ABCD[seq[j]]
            print(A,B,C,D)
            #ABまで位置を合わせる、AB->CDの順で印字
            if (i>>j) & 1:
                tmp+=(makeDistance(y,x,A,B)/S)
                y=C
                x=D
            #CDまで位置を合わせる、CD->ABの順で印字
            else:
                tmp += (makeDistance(y, x, C, D)/S)
                y = A
                x = B
            tmp+=makeDistance(A,B,C,D)/T
        
        ans = min(ans, tmp)
print(ans)
            

                
            
        