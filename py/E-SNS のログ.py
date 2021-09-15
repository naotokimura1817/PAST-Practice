N, Q = list(map(int, input().split()))

#  NxNのグラフを作る
graph = []
for i in range(0, N):
    row = []
    for j in range(0, N):
        row.append("N")
    graph.append(row)

# クエリを受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))

    # フォロー
    if query[0] == 1:
        a = query[1]
        b = query[2]

        a -= 1
        b -= 1

        # aがbをフォロー
        graph[a][b] = "Y"

    # フォロー全返し
    if query[0] == 2:
        a = query[1]

        a -= 1

        for j in range(0, N):
            if graph[j][a] == "Y":
                graph[a][j] = "Y"

    # フォローフォロー
    if query[0] == 3:
        a = query[1]

        a -= 1

        M = []

        for j in range(0, N):
            if graph[a][j] == "Y":
                for k in range(0, N):
                    if graph[j][k] == "Y" and k != a:
                        M.append(a)
                        M.append(k)

        for j in range(0, len(M), 2):
            graph[M[j]][M[j + 1]] = "Y"

for i in range(0, N):
    for j in range(0, N):
        if j == N-1:
            print(graph[i][j])
        else:
            print(graph[i][j], end='')

