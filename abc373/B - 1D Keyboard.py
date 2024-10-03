def calculate_distance(s):
    # 各アルファベットの位置を記録する辞書を作成
    positions = {char: i for i, char in enumerate(s)}

    # AからZまでのアルファベット
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 初期の位置と距離
    total_distance = 0
    current_position = positions[alphabet[0]]  # Aの位置

    # AからZまで順に距離を計算
    for char in alphabet[1:]:
        next_position = positions[char]
        total_distance += abs(next_position - current_position)
        current_position = next_position

    return total_distance

# アルファベットがごちゃごちゃに並んでいる例
s = input()
distance = calculate_distance(s)
print(distance)
