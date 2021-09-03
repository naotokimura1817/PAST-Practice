# This code was referenced to "アルゴリズム実技検定　公式テキスト　(ISBN：978-4-8399-7277-6)".

# # 隣接行列を使った解法
# N, M, Q = map(int, input().split())
#
# # N x NのFalseの2次元配列を作る
# graph = []
# for i in range(0, N):
#     # 長さNのFalseの1次元配列を作る
#     row = []
#     for j in range(0, N):
#         row.append(False)
#
#     # 長さNのFalseの1次元配列をgraphに追加する
#     graph.append(row)
#
# # M本の辺を受け取る
# for i in range(0, M):
#     u, v = map(int, input().split())
#
#     # Pythonで扱いやすくするため、頂点番号を全て-1する
#     u -= 1
#     v -= 1
#
#     # uとvの間には辺があるためgraphをTrueにする
#     graph[u][v] = True
#     graph[v][u] = True  # 逆もしかり
#
# # 頂点の色のリストを受け取る
# C = list(map(int, input().split()))
#
# # Q個のクエリを受け取る
# for i in range(0, Q):
#     query = list(map(int, input().split()))
#
#     # スプリンクラーを起動するクエリ
#     if query[0] == 1:
#         x = query[1]    # 起動するスプリンクラー情報を取得
#
#         # Pythonで扱いやすくするため、頂点番号を全て-1する
#         x -= 1
#
#         print(C[x]) # スプリンクラーxの色を出力
#
#         # 隣接するスプリンクラーを探す。
#         # すべてのスプリンクラー（グラフの頂点）を見る
#         for i in range(0, N):
#
#             # スプリンクラー同士をつなぐ辺が存在＝graph[x][i]がTrueならば色を変える
#             if graph[x][i]:
#                 C[i] = C[x]
#
#     # スプリンクラーを起動しないクエリ
#     if query[0] == 2:
#         x = query[1]
#         y = query[2]
#
#         # Pythonで扱いやすくするため、頂点番号を全て-1する
#         x -= 1
#
#         print(C[x])
#
#         # 頂点xの色をyに塗り替える
#         C[x] = y


# 隣接リストを使った解法
N, M, Q = map(int, input().split())

# N x 0の2次元配列を作る
graph = []

for i in range(0, N):
    # 長さ0の1次元配列を作る
    row = []
    graph.append(row)

# M本の辺を受け取る
for i in range(0, M):
    u, v = map(int, input().split())

    # Pythonで扱いやすくするため、頂点番号を全て-1する
    u -= 1
    v -= 1

    # 頂点uからvへ辺がある
    # （ある頂点に対して辺でつながった先の頂点を配列に格納していく）
    graph[u].append(v)
    # 頂点vからuへ辺がある
    graph[v].append(u)

C = list(map(int, input().split()))

# Q個のクエリを受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))

    # スプリンクラーを起動するクエリ
    if query[0] == 1:
        x = query[1]

        x -= 1

        print(C[x])

        # graph[x]に入っている（隣接した）頂点の色を変更する
        for i in graph[x]:
            C[i] = C[x]

    # スプリンクラーを起動しないクエリ
    if query[0] == 2:
        x = query[1]
        y = query[2]

        x -= 1

        print(C[x])

        C[x] = y











