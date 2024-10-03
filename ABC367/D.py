from collections import deque

# 入力部分
N, M = map(int, input().split())
U = [None] * M
V = [None] * M
W = [None] * M
G = [[] for _ in range(N + 1)]  # 隣接リストの初期化

# 有向辺の情報を読み込み、隣接リストを構築
for i in range(M):
    U[i], V[i], W[i] = map(int, input().split())
    G[U[i]].append((V[i], W[i]))  # 有向辺のみを追加

def find_vertex_values(N, G):
    # 頂点の値を格納する辞書
    values = {}

    # すべての頂点に対して連結成分を探索
    for start in range(1, N + 1):
        # 既に訪問した頂点はスキップ
        if start in values:
            continue

        # BFS用のキュー
        queue = deque([start])
        values[start] = 0  # 始点を0に設定
        # BFSで各頂点の値を決定
        while queue:
            current = queue.popleft()
            current_value = values[current]
            
            # 隣接する頂点を探索
            for neighbor, weight in G[current]:
                # 未訪問の頂点なら値を設定
                values[neighbor] = current_value + weight
                queue.append(neighbor)
    print(values)
    # 結果をリスト形式で取得
    result = [values[i] for i in range(1, N + 1)]
    return result

# グラフの頂点値を計算し出力
result = find_vertex_values(N, G)
print(*result)
