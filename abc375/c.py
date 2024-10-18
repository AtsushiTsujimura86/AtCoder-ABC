import itertools
import copy

N=int(input())
A=[list(input()) for _ in range(N)]
result = copy.deepcopy(A)
# result = A[:]

for i in range(N//2):
    if i==0:
        for x in range(i,N+1-i-1):
            for y in range(i,N+1-i-1):
                result[y][N+1-x-2] = A[x][y]
    else:
        result2 = copy.deepcopy(result)
        for x in range(i,N+1-i-1):
            for y in range(i,N+1-i-1):
                result[y][N+1-x-2] = result2[x][y]
                
                print(x,y)
                for row in result:
                    print("".join(row))
                    
        
for row in result:
    print("".join(row))