N = int(input())
words = []
for i in range(N):
    words.append(input())

max_len = 0
for i in range(N):
    max_len = len(words[i]) if max_len < len(words[i]) else max_len
M=max_len

words = words[::-1]
result = [""]*M
for i in range(M):
    for j in range(N):
        if len(words[j])-1 >= i:
            result[i] += words[j][i]
        else:
            result[i] += "*"
            
#条件に合うように*を除去
for i in range(M):
    while True:
        if result[i][-1] == "*":
            result[i] = result[i][:-1]
        else:
            break
        
print("\n".join(result))
        