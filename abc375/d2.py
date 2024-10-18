import itertools
s=input()
if len(s) < 3:
    print(0)
    exit()
    
cnt=0

left = {chr(ord("A")+i):0 for i in range(26)}
right = {chr(ord("A")+i):0 for i in range(26)}
#前処理
left[s[0]] += 1
for i in list(s[2:]):
    right[i] +=1
    
for j in range(1,len(s)-1):
    for key in left:
        if left[key]>0:
            cnt+=left[key]*right[key]
    #処理後
    #s[j]をleftから取り除く
    #jをずらしたときにS[j]を
    left[s[j]]+=1
    right[s[j+1]]-=1
print(cnt)
            