# This code was referenced to "アルゴリズム実技検定　公式テキスト　(ISBN：978-4-8399-7277-6)".

N = int(input())

ans = 0


# 数nについて調べ、末尾に数字を追加した数を再帰的に調べる関数を作る
# use3, use5, use7はそれぞれ、3、5、7を使ったかどうかというフラグ
def dfs(n, use3, use5, use7):
    global ans

    # Nを超えていたら探索を打ち切って終了する
    if n > N:
        return

    # 3種類すべてを使っていたら答えに加算する
    if use3 and use5 and use7:
        ans += 1

    # 末尾に3,5,7を付けた数を再帰的に調べる
    dfs(10 * n + 3, True, use5, use7)
    dfs(10 * n + 5, use3, True, use7)
    dfs(10 * n + 7, use3, use5, True)


# 何もない状態から関数を呼び出す
dfs(0, False, False, False)

print(ans)
