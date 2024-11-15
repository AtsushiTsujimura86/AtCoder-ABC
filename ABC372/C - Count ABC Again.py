N, Q = map(int, input().split())
S = list(input())
pos = [None]*Q
words = [None]*Q
for i in range(Q):
    user_input=list(input().split())
    pos[i],words[i] = int(user_input[0]), user_input[1]
for i in range(Q):
    S[pos[i]-1] = words[i]
 


