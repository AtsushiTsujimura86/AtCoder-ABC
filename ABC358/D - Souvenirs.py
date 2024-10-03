N,M = map(int,input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()
B.sort()
s=0
result=[]
i=0
for j in range(N):
    print(i,j)
    if B[i] <= A[j]:
        result.append(A[j])
        i+=1
    if i>=M:
        break
    
# for i in range(M):
#     print(f"i:{i}, j:{j}")
#     if B[i] <= A[j]:
#         result.append(A[j])
#         continue
#     j+=1
#     if j >= N:
#         print(-1)
#         exit()
    # for j in range(s,N):
    #     print(f"i:{i}, j:{j}")
    #     if B[i] <= A[j]:
    #         result.append(A[j])
    #         s=j+1
    #         break
if len(result) < M:
    print(-1)
else:
    print(sum(result))
