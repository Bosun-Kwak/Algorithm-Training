import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

chicken = [] # 치킨집이 있는 좌표
home = [] # 집이 있는 좌표
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i, j))
        if board[i][j] == 1:
            home.append((i, j))
# print(chicken)
# print(home)

min_val = 1e9
chick = []
def home2chick(chick):
    h2cMin = 0
    for hx,hy in home:
        h2chicks = []
        for c in chick:
            cx, cy = chicken[c]
            h2chicks.append(abs(hx-cx)+abs(hy-cy))
        h2cMin += min(h2chicks)


    return h2cMin
def find_ans(cur,chick):
    global min_val
    if len(chick)==m:

        val = home2chick(chick)
        min_val = min(min_val, val)
    if cur == len(chicken):
        return

    chick.append(cur)
    find_ans(cur+1,chick)
    chick.pop()
    find_ans(cur+1,chick)

find_ans(0,chick)
print(min_val)