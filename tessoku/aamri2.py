import time

def power(a,b,n):
    ans=1
    for i in range(0,b):
        ans = ans*a % n
    return ans

def power2(a,b,n):
    ans = a**b
    return ans % n
# start = time.time()
# print(power(2,42,1000000007))
# end=time.time()
# print((f"実行時間: {(end-start):.12f}秒"))
start=time.time()
print(power2(2,42,1000000007))
end=time.time()
print((f"実行時間: {(end-start):.10f}秒"))