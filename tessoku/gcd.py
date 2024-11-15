def gcd(a,b):
    if a==b:
        return a
    if a>b:
        return gcd(b,a-b)
    else:
        return gcd(a,b-a)

print(gcd(28,49))
