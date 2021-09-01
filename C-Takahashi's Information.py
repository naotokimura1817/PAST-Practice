A = []
cnt = 0

# input
for _ in range(0, 3):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(0, 2):
    # col - col
    x = A[0][i] - A[0][i + 1]
    y = A[1][i] - A[1][i + 1]
    z = A[2][i] - A[2][i + 1]
    if x == y == z:
        cnt += 1

for i in range(0, 2):
    # row - row
    x = A[i][0] - A[i + 1][0]
    y = A[i][1] - A[i + 1][1]
    z = A[i][2] - A[i + 1][2]
    if x == y == z:
        cnt += 1

if cnt == 4:
    print("Yes")
else:
    print("No")
