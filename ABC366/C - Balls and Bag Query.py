Q = int(input())
num_set = set()
result = []

for i in range(Q):
    # print("num_set:", num_set)
    query = list(map(int, input().split()))
    if(len(query) == 2):        
        if query[0] == 1:
            num_set.add(query[1])
        else:
            num_set.discard(query[1])
    else:
        result.append(len(num_set))

print("\n".join(map(str, result)))