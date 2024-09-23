N = int(input())
# array = [[0]*N for _ in range(N**2)]
# print(array)
array = [[0]*(N+1)]
for i in range(N**2):
    num_input = list(map(int, input().split()))
    num_input.insert(0,0)
    array.append(num_input)
Q = int(input())
result=[]
for i in range(Q):
    xl,xr,yl,yr,zl,zr = map(int, input().split())
    total=0
    for i in range(xl, xr+1):
        for j in range(yl, yr+1):
            for k in range(zl, zr+1):
                print("arrayの要素",array[i*j][k])
                total+=array[i*j][k]
    result.append(total)

print("\n".join(map(str, result)))