from itertools import product

N = int(input())
L=[None]*N
R=[None]*N
for i in range(N):
    L[i], R[i] = map(int, input().split())
X = [None]*N

left_sum = 0
right_sum = 0
for i in range(N):
    left_sum += L[i]
    right_sum += R[i]
if(left_sum <= 0 <= right_sum):
    print("Yes")
else:
    print("No")
    exit()

rangelist = []
for i in range(N):
    sublist = [] 
    for j in range(L[i], R[i]+1):
        sublist.append(j)
    rangelist.append(sublist)

def find_zero_sum_combination(matrix):
    for combination in product(*matrix):
        if sum(combination) == 0:
            return combination
    return None

print(find_zero_sum_combination(rangelist))