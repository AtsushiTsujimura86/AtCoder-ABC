
N = int(input())
H = list(map(int, input().split()))
t = 0
i = 0
    
while(i<N):
    #今のtを確認
    if t%3 == 0:
        pass
    elif t%3==1:
        if H[i] > 1:
            t+=2
            H[i]-=4
        elif H[i] == 1:
            t+=1
            H[i]-=1
    else:
        t+=1
        H[i]-=3
    
    if(H[i] > 0):        
        t += 3*(H[i] // 5)
        if(H[i]%5 != 0):
            if(H[i]%5 == 1):
                t+=1
            elif(H[i]%5 == 2):
                t+=2
            else:
                t+=3
    i+=1    
    
print(t)