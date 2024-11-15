N, K = map(int, input().split())
R = list(map(int, input().split()))

nums = []
for i in range(N):
    num=[]
    for j in range(1,R[i]+1):
        num.append(j)
    nums.append(num)
        
from itertools import product

def find_valid_combinations(arrays, k):
    # 各配列から1つずつ要素を取り出して全ての組み合わせを生成
    combinations = list(product(*arrays))
    print(combinations)
    
    # 総和がkの倍数である組み合わせを格納するリスト
    valid_combinations = []
    
    # 各組み合わせの総和を計算し、kの倍数かどうかを判定
    for combination in combinations:
        total = sum(combination)
        if total % k == 0:
            valid_combinations.append(combination)
    
    return valid_combinations

result = find_valid_combinations(nums, K)
for i in range(len(result)):
    # print(" ".join(str, result[i]))
    print(*result[i])