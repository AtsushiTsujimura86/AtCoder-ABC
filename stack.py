#pythonでスタックを実装
from collections import deque
N=int(input())
codes = [None]*N
words = [""]*N
for i in range(N):
    codes[i] = input()
    if codes[i].split()[0] == "1":
        words[i] = codes[i].split()[1]
        codes[i] = codes[i].split()[0]

s = []
for i in range(N):
    if codes[i] == "1":
        s.append(words[i])
    elif codes[i] == "2":
        print(s[-1])
    else:
        s.remove(s[-1])
