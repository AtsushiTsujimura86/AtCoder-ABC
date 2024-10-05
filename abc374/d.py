N,S,T=map(int,input().split())
lst = []
for i in range(N):
    a,b,c,d=map(int, input().split())
    lst.append([a,b])
    lst.append([c,d])
print(lst)

distances = [[0 for _ in range(2*N)] for _ in range(2*N)]
for i in range(2*N):
    for j in range(2*N):
        distances[i][j] = ((lst[i][0]-lst[j][0])**2 + (lst[i][1]-lst[j][1])**2)**0.5
print(distances)

existance = [i for i in range(2*N)]
print(existance)
#(0.0)と一番近いやつ探す
result=0
start_index = lst.index(min(lst))
result+=sum(min(lst))*S
#行先
if start_index%2==0:
    end_index = start_index+1
else:
    end_index=start_index-1
result+=distances[start_index][end_index]*T
existance.remove(start_index)
existance.remove(end_index)
#次の行先
while existance:
    #今のend_indexに一番近いやつ
    for i in range(2*N):
        min_num=10**18
        if not i in existance:
            continue
        else: 
            if min_num > distances[end_index][i]:
                min_num=distances[end_index][i]
                start_index=i
    #Sで移動
    result+=distances[end_index][start_index]*S
    if start_index%2==0:
        end_index = start_index+1
    else:
        end_index=start_index-1
    result+=distances[start_index][end_index]*T    
    existance.remove(start_index)
    existance.remove(end_index)

print(result)
    