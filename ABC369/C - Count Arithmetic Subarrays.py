N = int(input())
A = list(map(int, input().split()))

tousa_cnt = 0
div_list = [0]*(N-1)
for i in range(N-1):
    div_list[i] = A[i+1] - A[i]

for i in range(N-1):
    for j in range(i,N-1):
        if div_list[i] == div_list[j]:
            tousa_cnt += 1
        else:
            break   
    
print(tousa_cnt + N)

