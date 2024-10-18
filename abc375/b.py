n = int(input())
X=[0]*n
Y=[0]*n
for i in range(n):
    X[i],Y[i] = map(int, input().split())

def distance(a,b,c,d):
    return ((a-c)**2 + (b-d)**2)**0.5

total = distance(0,0,X[0],Y[0])
if n==1:
    total *=2
    print(total)
    exit()
else:
    for i in range(n-1):
        total += distance(X[i],Y[i],X[i+1],Y[i+1])


total += distance(X[i+1],Y[i+1],0,0)
print(total)