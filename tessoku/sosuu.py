def IsSosuu(n):
    if n==1:
        return None
    for i in range(2,n):
        if n%i == 0:
            return None
    return True

print(IsSosuu(17))
print(IsSosuu(31))
print(IsSosuu(35))
print(IsSosuu(49))

def IsSosuu2(n):
    if n==1:
        return None
    print(int(n**0.5))
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return None
    return True

print(IsSosuu2(5))

#エラトステネスの篩
def  Eratosthenes(n):
    