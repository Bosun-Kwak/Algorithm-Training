board = [[0]*101 for _ in range(101)]

res = 0
for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx,rx):
        for y in range(ly,ry):
            board[x][y]=1

# print(board)
for row in board:
    res += sum(row)
print(res)