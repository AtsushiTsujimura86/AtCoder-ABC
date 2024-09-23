A = list(map(int, input().split()))
B = list(map(int, input().split()))

def checkSquares(A,B):
    a=A[0]
    b=A[1]
    c=A[2]
    d=A[3]
    e=A[4]
    f=A[5] 
    g=B[0]
    h=B[1]
    i=B[2] 
    j=B[3]
    k=B[4] 
    l=B[5]
    if(a <= g and g <= d) or (a <= j and j <= d) or (g<=a and d<=j):
        if(b <= h and h <= e) or (b <= k and k <= e) or (h<=b and e<=k):
            if(c <= i and i <= f) or (c <= l and l <= f) or (i<=c and f<=l):
                return True
    else: return None
                    
if(checkSquares(A,B) or checkSquares(B,A)):
    print("Yes")
else: print("No")