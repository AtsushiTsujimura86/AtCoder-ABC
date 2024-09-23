N = int(input())
A = list(map(int, input().split()))

B=A.copy()
B.pop(B.index(max(B)))
max_elm = max(B)
index = A.index(max_elm)+1

print(index)