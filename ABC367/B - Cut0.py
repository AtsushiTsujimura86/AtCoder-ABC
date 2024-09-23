X = input()
for i in range(len(X)):
    if X[i] == '.':
        break
dot_index = i
for i in reversed(range(1,4)):
    if X[dot_index + i] == '0':
         X = X[:-1]
    else:
        break    
    if X[-1] == '.':
        X = X[:-1]  
print(X)