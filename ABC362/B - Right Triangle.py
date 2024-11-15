X = [None]*3
Y = [None]*3
for i in range(3):
    X[i], Y[i] = map(int, input().split())
    
ab2 = (X[0]-X[1])**2 + (Y[0]-Y[1])**2
bc2 = (X[1]-X[2])**2 + (Y[1]-Y[2])**2
ca2 = (X[2]-X[0])**2 + (Y[2]-Y[0])**2

if ab2 == (bc2+ca2) or bc2 == (ca2+ab2) or ca2 == (ab2+bc2):
    print("Yes")
else:
    print("No")