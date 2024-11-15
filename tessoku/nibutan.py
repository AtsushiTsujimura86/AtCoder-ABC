lst = [1,2,3,4,5,6,7,8,9,10]
def nibutan(lst, x):
    left = 0
    right = len(lst)-1
    while left<right:
        mid=(left+right)//2
        print(f"left: {lst[left]}, right: {lst[right]}, mid: {lst[mid]}")
        if x>lst[mid]:
            left=mid+1
        else:
            right=mid
    return left

def nibutan2(lst, x):
    left = 0
    right = len(lst)-1
    while left<right:
        mid=(left+right)//2
        print(f"left: {lst[left]}, right: {lst[right]}, mid: {lst[mid]}")
        if x>lst[mid]:
            left=mid+1
        else:
            right=mid
    return right-1
print(nibutan(lst, 3))

lst = [i for i in range(0,20,2)]
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#n以上m以下に含まれている要素
n=4
m=14
print(nibutan(lst, n))