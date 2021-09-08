# This code was referenced to "アルゴリズム実技検定　公式テキスト　(ISBN：978-4-8399-7277-6)".

N = int(input())
h = list(map(int, input().split()))

# cost[i]：足場iにたどり着くための最小コスト。サイズをNとする
cost = [0] * N

# 初期条件
cost[0] = 0

# 二つ目の足場はジャンプ元が1通り
cost[1] = cost[0] + abs(h[0] - h[1])

# 三つ目の足場以降はジャンプ元が二通りあるため、コストが小さい方を採用する
for i in range(2, N):
    cost[i] = min(cost[i - 1] + abs(h[i - 1] - h[i]), cost[i - 2] + abs(h[i - 2] - h[i]))

# 答えは最後の足場までの最小コスト
print(cost[N - 1])


