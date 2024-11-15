N, Q = map(int, input().split())
S = list(input())
pos = [None] * Q
words = [None] * Q

# 初期状態で "ABC" のカウントを取得
def count_abc(S, start, end):
    cnt = 0
    for i in range(start, min(end, N - 2)):
        if S[i:i+3] == ['A', 'B', 'C']:
            cnt += 1
    return cnt

# 初期状態で "ABC" のパターンを数える
cnt = count_abc(S, 0, N)

# 各クエリに対する処理
for i in range(Q):
    p = int(pos[i]) - 1
    w = words[i]
    
    # 変更される位置の前後2文字分だけ"ABC"を再チェック
    # まずは変更前のカウントを減らす
    cnt -= count_abc(S, max(0, p - 2), min(p + 1, N - 2))
    
    # 文字を更新
    S[p] = w
    
    # 変更後のカウントを加える
    cnt += count_abc(S, max(0, p - 2), min(p + 1, N - 2))
    
    # 結果を出力
    print(cnt)