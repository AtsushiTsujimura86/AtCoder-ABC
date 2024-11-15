N = int(input())  # ビルの数
H = list(map(int, input().split()))  

s=[] #スタック
result = [] #結果リスト、いくつのビルが見えるか

for h in H[::-1]:
    result.append(len(s))
    #
    while s and s[-1]<h:
        s.pop()
    s.append(h)

print(*result[::-1])