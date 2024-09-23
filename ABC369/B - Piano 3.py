N = int(input())
A = [0] * N
S  = [0] * N
for i in range(N):
    a = list(input().split())
    A[i], S[i] = int(a[0]), a[1]     

hirou = 0
l_pos = 0
r_pos = 0
l_cnt = 0
r_cnt = 0
for i in range(N):
    hand = S[i]
    if hand == "L":
        if l_cnt != 0:
            hirou += max(l_pos,A[i]) - min(l_pos, A[i])
            l_pos = A[i]
        else:
            l_pos = A[i]
            l_cnt += 1
    else:
        if r_cnt != 0:
            hirou += max(r_pos,A[i]) - min(r_pos, A[i])
            r_pos = A[i]
        else:
            r_pos = A[i]
            r_cnt += 1

print(hirou)