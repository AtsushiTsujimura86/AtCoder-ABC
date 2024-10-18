N=int(input())
S = input()
cnt = 0
i=0
while i < N-2:
    if S[i] == "#" and S[i+2] == "#" and S[i+1] == ".":
        cnt+=1
        i += 2
    else:
        i+=1
print(cnt)
            