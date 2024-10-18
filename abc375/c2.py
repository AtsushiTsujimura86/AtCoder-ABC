import itertools

N = int(input())
A = [list(input()) for _ in range(N)]
result = [row[:] for row in A]

for x, y in itertools.product(range(N), repeat=2):
    new_x, new_y = y, N - 1 - x
    result[new_y][new_x] = A[x][y]

for row in result:
    print("".join(row))