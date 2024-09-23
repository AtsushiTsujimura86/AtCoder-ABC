def f(n):
    print("n:", n)
    if n == 0:
        return ["#"]
    sub = f(n - 1)
    l = len(sub)
    ret = [["." for j in range(3 * l)] for i in range(3 * l)]
    for I in range(3):
        for J in range(3):
            if I != 1 or J != 1:
                for i in range(l):
                    for j in range(l):
                        ret[I * l + i][J * l + j] = sub[i][j]
    return ret


ans = f(int(input()))
for a in ans:
    print("".join(a))
