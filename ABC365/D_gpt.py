def max_wins(N, S):
    # DP配列の初期化
    # dp[i][j] は i回目に j を出したときの勝利回数の最大値を表す
    # j = 0: グー, j = 1: チョキ, j = 2: パー
    dp = [[0] * 3 for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(3):
            if j == 0:  # グーを出す場合
                dp[i][0] = max(dp[i][0], dp[i-1][1], dp[i-1][2])
                if S[i-1] == 'S':  # 青木君がチョキなら勝つ
                    dp[i][0] += 1
            elif j == 1:  # チョキを出す場合
                dp[i][1] = max(dp[i][1], dp[i-1][0], dp[i-1][2])
                if S[i-1] == 'P':  # 青木君がパーなら勝つ
                    dp[i][1] += 1
            elif j == 2:  # パーを出す場合
                dp[i][2] = max(dp[i][2], dp[i-1][0], dp[i-1][1])
                if S[i-1] == 'R':  # 青木君がグーなら勝つ
                    dp[i][2] += 1

    # 最後のじゃんけんで出す手の最大勝利数を求める
    return max(dp[N])

# 使用例
N = int(input())
S = input()
print(max_wins(N, S))  # 出力: 3
