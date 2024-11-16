from bisect import bisect_right
li = [0,0, 1,1,1,2,2]
idx = bisect_right(li, 1, 0)
print(idx)
