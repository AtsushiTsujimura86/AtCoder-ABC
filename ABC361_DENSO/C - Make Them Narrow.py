N, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
print(A)
def emptyList(A):
    if(len(A) == 0):
        print(0)
        exit()
    
def calcGap(A):
    B = A[:]
    #最大値と２番目の最大値の差をとる
    maxA = B[-1]
    B.remove(maxA)
    emptyList(B)
    maxA2 = B[-1]
    gap_max = maxA-maxA2
    #最小値と２番目の最小値の差をとる
    minA = B[0]
    B.remove(minA)
    emptyList(B)
    minA2 = B[0]
    gap_min = minA2-minA
    if(gap_max >= gap_min):
        del A[-1]
    else:
        del A[0]
    return A
    
    

for i in range(k):
    A = calcGap(A)
print(max(A) - min(A))    