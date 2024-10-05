S=input()
T=input()
if len(S) > len(T):
    T += "%"*(len(S)-len(T))
elif len(S) < len(T):
    S+= "%"*(len(T)-len(S))
    

if S==T:
    print(0)
else:
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            exit()