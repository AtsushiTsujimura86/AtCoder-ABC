Q = int(input())
num_dict = {}
result = []

for i in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 2:
        if query[0] == 1:
            # 数字を追加（存在しない場合は1、存在する場合はカウントを増加）
            num_dict[query[1]] = num_dict.get(query[1], 0) + 1
        else:
            # 数字を削除（カウントを減少、0になったら削除）
            if query[1] in num_dict:
                num_dict[query[1]] -= 1
                if num_dict[query[1]] == 0:
                    del num_dict[query[1]]
    else:
        result.append(len(num_dict))

print("\n".join(map(str, result)))
