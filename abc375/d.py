s=input()
sum = {chr(i + ord("A")) : [] for i in range(26)}
for i, s_i in enumerate(s):
    sum[s_i].append(i)

cnt=0
for key in sum:
    while len(sum[key]) > 1:
        cnt += sum[key][-1] - sum[key][-2] -1
        sum[key].pop()
print(cnt)