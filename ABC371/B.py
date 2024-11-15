def find_exponents(M):
    result = []
    n = 0
    power_sum = 0

    # 3の累乗を加算し、Mを超えるまで続ける
    while power_sum < M:
        power_sum += 3 ** n
        if power_sum <= M:
            result.append(n)
        n += 1

    # 最後に、合計がMに等しいか確認
    if power_sum == M:
        return result
    else:
        return []  # Mを正確に表せない場合

# 入力を取得
M = int(input("Mを入力してください: "))
result = find_exponents(M)

# 結果を出力
if result:
    print(" ".join(map(str, result)))
else:
    print("解が見つかりませんでした")
