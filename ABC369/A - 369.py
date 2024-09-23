A,B = map(int, input().split())
div = max(A,B) - min(A,B)
low_num = min(A,B) -div
high_num = max(A,B) + (div)
if low_num == high_num:
    print(1)
    exit()
if (A+B) % 2 == 0:
    print(3)
else:
    print(2)
