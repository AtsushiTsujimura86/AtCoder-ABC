N=int(input())
X=list(map(int, input().split()))
P=list(map(int, input().split()))
Q=int(input())
L,R = [None]*Q,[None]*Q
for i in range(Q):
    L[i],R[i] = map(int, input().split())
    
RUI = [P[0]]
for i in range(1,N):
    RUI.append(RUI[i-1] + P[i])

def find_start_index(lst, value):
    left, right = 0, len(lst) - 1
    
    # 二分探索
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < value:
            left = mid + 1
        else:
            right = mid
    
    return left

def find_end_index(lst, value):
    left, right = 0, len(lst) - 1
    
    # 二分探索
    while left < right:
        mid = (left + right) // 2
        if lst[mid] == value:
            return l
        
        if lst[mid] < value:
            left = mid + 1
        else:
            right = mid
    
    return left

def get_end_index(lst, target):
    # リストが空の場合
    if not lst:
        return None

    # 二分探索の範囲を定義
    left, right = 0, len(lst) - 1
    best_index = -1  # 近い値のインデックスを保存

    # 二分探索
    while left <= right:
        mid = (left + right) // 2

        # target 以下の値を記録する
        if lst[mid] <= target:
            best_index = mid
            left = mid + 1  # 右側を探索
        else:
            right = mid - 1  # 左側を探索

    return best_index

def getIndexfromPos(pos):
    for i in range(N):
        if X[i] == pos:
            return i
    return None

#クエリ
for i in range(Q):
    l,r=L[i],R[i]
    #l以上r以下の村の総人口を求める
    #i以上r以下の村を特定
    #二分探索で開始位置、終了位置を特定

    if l==r:
        if l not in X:
            print(0)
        else:
            print(P[getIndexfromPos(l)])
    else:
        start_index = find_start_index(X, l)
        end_index = get_end_index(X, r)
        if start_index-1 < 0:
            result = RUI[end_index]
        else:
            result = RUI[end_index]-RUI[start_index-1]
        print(result)
        
    
