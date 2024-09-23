S = input()
len_s = len(S)

up_cnt = 0
nums = [i for i in range(len_s)]
up_index = []
for i in range(len_s):
    if S[i].isupper():
        up_index.append(i)
        up_cnt += 1

#差集合をとる
lower_index = [i for i in nums if i not in up_index]
S_list = list(S)

#小文字の方が多いとき
if len_s > up_cnt*2:
    for i in up_index:
        S_list[i] = S[i].lower()
else:
    for i in lower_index:
        S_list[i] = S[i].upper()
    
print("".join(S_list))