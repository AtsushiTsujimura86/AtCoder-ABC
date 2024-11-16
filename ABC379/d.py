Q=int(input())
for i in range(Q):
    q = input().split()
    print(q)
    print(type(q))
    if q[0] == "1":
        print("queue")
    elif q[0] == "2":
        print("day++", q[1])
    else:
        print("print cnt", q[1])
