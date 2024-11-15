A, B, C = map(int, input().split())
if B > C:
    A+=24
    C+=24
if B<=A and A<=C:
    print("No")
else:
    print("Yes")