import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]
# 우, 하, 우하, 우상
dxy = [(0,1),(1,0),(1,1),(-1,1)]

for i in range(19):
    for j in range(19):
        if board[i][j] !=0:
            color = board[i][j]

            for d in range(4):
                cnt = 1
                dx,dy = dxy[d]
                nx = i+dx
                ny = j+dy
                while True:
                    if nx<0 or nx>=19 or ny<0 or ny>=19 or board[nx][ny]!=color:
                        break
                    cnt+=1
                    if cnt == 5:
                        if 0<=i-dx<19 and 0<=j-dy<19 and board[i-dx][j-dy] == color:
                            break
                        if 0<=nx+dx<19 and 0<=ny+dy<19 and board[nx+dx][ny+dy] == color:
                            break
                        print(color)
                        print(i+1, j+1)
                        sys.exit(0)
                    nx+= dx
                    ny+= dy
print("0")