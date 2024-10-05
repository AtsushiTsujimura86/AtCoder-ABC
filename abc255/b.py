N,K=map(int, input().split())
A=list(map(int, input().split()))
X=[None]*N
Y=[None]*N

for i in range(N):
    X[i],Y[i] = map(int, input().split())
print()
distances = [[0 for _ in range(N)] for _ in range(K)]
for i in range(K):
    for j in range(N):
        distances[i][j] = abs(((X[j]-X[A[i]-1])**2 + (Y[j]-Y[A[i]-1])**2)**(0.5))
print(distances)

transposed_distances = [list(row) for row in zip(*distances)]
print(transposed_distances)
result = []
for i in range(N):
    min_val = min(transposed_distances[i])
    result.append(min_val)

print(result)
print(max(result))