# Python 3.8.2ではTLE
# PyPy3 7.3.0ではAC

N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

# cost[i]：足場iにたどり着くための最小コスト。サイズをNとする
cost = [0] * N

# 初期条件
cost[0] = 0
c = 0

for i in range(1, N):
    c = (cost[i - 1] + abs(h[i - 1] - h[i]))
    for j in range(2, K + 1):
        if i - j < 0:
            continue

        d = (cost[i - j] + abs(h[i - j] - h[i]))

        if c > d:
            c = d
    cost[i] = c

# 答えは最後の足場までの最小コスト
print(cost[N - 1])
