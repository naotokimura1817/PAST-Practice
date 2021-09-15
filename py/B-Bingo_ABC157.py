card = []  # Bingo card
rcard = []  # Bingo result card
nums = []  # Bingo numbers

# ビンゴカードの作成
for _ in range(0, 3):
    # 一行ずつ読み取る
    row = list(map(int, input().split()))
    # card配列に足していく
    card.append(row)

# ビンゴ数字の入力
n = int(input())  # Number of bingo numbers
for _ in range(0, n):
    num = int(input())
    nums.append(num)

# ビンゴ結果のカード
for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(False)
    rcard.append(row)

# ビンゴカードの番号とビンゴ番号を比較する
for i in range(0, len(nums)):
    for j in range(0, 3):
        for k in range(0, 3):
            if card[j][k] == nums[i]:
                rcard[j][k] = True

bingo = False   # Bingo flag

for i in range(0, 3):
    if rcard[i][0] and rcard[i][1] and rcard[i][2]:
        bingo = True

for i in range(0, 3):
    if rcard[0][i] and rcard[1][i] and rcard[2][i]:
        bingo = True

if rcard[0][0] and rcard[1][1] and rcard[2][2]:
    bingo = True

if rcard[0][2] and rcard[1][1] and rcard[2][0]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")
