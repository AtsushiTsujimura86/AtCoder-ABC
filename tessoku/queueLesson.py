from collections import deque
N=int(input())
codes=[0]*N
names=[""]*N
for i in range(N):
    user_input = list(input().split())
    codes[i] = user_input[0]
    if codes[i] == "1":
        names[i] = user_input[1]

queue = deque([])
for i in range(N):
    print(queue)
    if codes[i] == "1":
        queue.append(names[i])
    elif codes[i] == "2":
        print(queue[0])
    else:
        queue.remove(queue[0])

