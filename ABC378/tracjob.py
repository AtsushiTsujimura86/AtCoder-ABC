#さいころの定義
n,m,q =map(int, input().split())
s=[0 for _ in range(q)]
t=[0 for _ in range(q)]
x=[0 for _ in range(q)]
for i in range(q):
    s[i], t[i], x[i] = map(int, input().split())

class Dice:
    def __init__(self):
        #上、下、手前、奥、左、右
        self.faces = [1,6,2,5,3,4]
    def roll_right(self):
        faces = self.faces
        self.faces = [faces[4], faces[5], faces[2], faces[3], faces[1], faces[0]]
    def roll_left(self):
        faces = self.faces
        self.faces = [faces[5], faces[4], faces[2], faces[3], faces[0], faces[1]]
    def roll_flont(self):
        faces = self.faces
        self.faces = [faces[2], faces[3], faces[1], faces[0], faces[4], faces[5]]
    def roll_back(self):
        faces = self.faces
        self.faces = [faces[3], faces[2], faces[0], faces[1], faces[4], faces[5]]
    def get_up_face(self):
        return self.faces[0]

dice = Dice()
#n-1, m-1まで行けるか
cnt=0
min_k=10**18
visited=[[False]*m for _ in range(n)]

#深さ有線探索で
def dfs(i,j,k,face):
    global min_k
    if i==n-1 and j==m-1:
        min_k = min(min_k, k)
        return
    visited[i][j] = True
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni,nj = i+di, j+dj           
        if 0<=ni<n and 0<=nj<m and not visited[ni][nj]:
            #さいころの目の変更
            #下に移動
            if di==1 and dj==0:
                dice.roll_back()
            #右に移動
            elif di==0 and dj==1:
                dice.roll_right()
            #上に移動
            elif di==-1 and dj == 0:
                dice.roll_flont()
            #左に移動
            else:
                dice.roll_left()  
            #マスの条件を満たしているかをチェック
            frag = True
            for qi in range(q):
                if s[qi] == ni and t[qi] == nj and dice.get_up_face()==x[qi]:
                    frag = False
                    #行き先が禁止マスだった場合、さいころの目を戻す
                    if di==1 and dj==0:
                        dice.roll_flont()
                    elif di==0 and dj==1:
                        dice.roll_left()
                    elif di==-1 and dj == 0:
                        dice.roll_back()
                    else:
                        dice.roll_right()
            if frag:                
                dfs(ni,nj,k+1,dice.get_up_face())
    
    
    visited[i][j] = False
    
dfs(0,0,0,dice.get_up_face())
if min_k == 10**18:
    print("NO")
else:
    print("YES")
    print(min_k)

        