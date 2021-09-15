# This code was referenced to "アルゴリズム実技検定　公式テキスト　(ISBN：978-4-8399-7277-6)".

# 再帰上限を増やす
import sys

sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))
S = []  # 迷路を格納
# 迷路を取得
for i in range(H):
    s = input()
    S.append(s)

# 始点と終点の座標を探し、それぞれ (si, sj) と (gi, gj) とする
for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            si, sj = i, j
        if S[i][j] == 'g':
            gi, gj = i, j

# 訪問済みかどうかを管理する2次元配列
visited = []
for i in range(H):
    visited.append([False] * W)


# 再帰関数dfsを定義する
def dfs(i, j):
    visited[i][j] = True

    # 4方向の隣マスを探索する
    for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        # もし盤面の範囲内でなければ無視する
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
        # もし壁マスであれば無視する
        if S[i2][j2] == '#':
            continue
        # もし未訪問であれば再帰的に呼び出す
        if not visited[i2][j2]:
            dfs(i2, j2)


# 始点から呼び出す
dfs(si, sj)

# 終点が訪問済みかどうかに応じてYesまたはNoを出力する
if visited[gi][gj]:
    print('Yes')
else:
    print('No')
