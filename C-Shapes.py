# Referenced to https://atcoder.jp/contests/abc218/editorial/2637

N = int(input())


# グリッドを読み込んで#の位置の集合を返す
def read():
    S = set()
    for y in range(N):
        l = input()
        for x in range(N):
            if l[x] == '#':
                S.add((x, y))
    return S


# SとTの中には、#の座標が格納されている
S = read()
T = read()

for _ in range(4):
    # 最も左（複数あればそのうちで最も上）の#を(0, 0)に移動する
    mx, my = min(S)
    S = set((x - mx, y - my) for x, y in S)
    mx, my = min(T)
    T = set((x - mx, y - my) for x, y in T)

    if S == T:
        print('Yes')
        exit(0) # プログラムを終了させる

    # Tを回転する
    T = set((y, -x) for x, y in T)

print('No')