A=list(input().split())
one = A.count("1")
two = A.count("2")
three = A.count("3")
four = A.count("4")
cnt=0
def solve(n, cnt):
    if A.count(n) == 4:
        cnt += 2
    elif A.count(n) == 3:
        cnt += 1
    elif A.count(n) == 2:
        cnt += 1

    return cnt
    
for string in ["1", "2", "3", "4"]:
    cnt = solve(string, cnt)
print(cnt)

