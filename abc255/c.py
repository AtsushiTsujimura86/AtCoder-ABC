x,a,d,n = map(int, input().split())
suretsu = [a+i*d for i in range(n)]
if d < 0:
    suretsu=suretsu[::-1]


#二分探索でxに最も近い値を探す
left=0
right=len(suretsu)-1
while left<=right:
    mid=(left+right)//2
    if x > suretsu[mid]:
        left=mid+1
    else:
        right=mid-1
if left < 0 or left > len(suretsu)-1:
    pos = right
elif right <0 or right > len(suretsu)-1:
    pos = left
else:
    if abs(suretsu[left] - x) > abs(suretsu[right]-x):
        pos = right
    else:
        pos=left

diff = x-suretsu[pos]
diff_abs = abs(diff)
print(diff_abs)
    