S1, S2, S3 = input().split()
a, b, c = 0,0,0
if S1 == ">":
    a+=1
    b-=1
else:
    a-=1
    b+=1
if S2 == ">":
    a+=1
    c-=1
else:
    a-=1
    c+=1
if S3 == ">":
    b+=1
    c-=1
else:
    b-=1
    c+=1
    
def second_largest_index(lst):
    if len(lst) < 2:
        return None  # 要素が2つ未満の場合はNoneを返す

    # リストを一旦セットにして最大値を取り除く
    largest = max(lst)
    filtered_lst = [x for x in lst if x != largest]

    if len(filtered_lst) == 0:
        return None  # 全て同じ値の場合

    second_largest = max(filtered_lst)  # 二番目に大きい値を取得
    return lst.index(second_largest)    # 二番目に大きい値のインデックスを返す

# 例
lst = [a,b,c]
index = second_largest_index(lst)
if index == 0:
    print("A")
elif index == 1:
    print("B")
else:
    print("C")

            