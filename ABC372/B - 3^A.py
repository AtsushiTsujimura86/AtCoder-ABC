import math
M=int(input())
lst = []


def calc(n, lst):
    i=1
    if n == 0:
        return lst

    while True:
        if n < i:
            i//=3
            break
        i*=3
    lst.append(i)
    print(n-i,math.log(i,3))
    return calc(n-i, lst)

lst = calc(M,lst)
result = [int(math.log(x,3)) for x in lst]
print(len(result))
print(" ".join(str(i) for i in result))
    