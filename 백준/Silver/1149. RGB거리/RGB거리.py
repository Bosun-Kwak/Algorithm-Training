# import sys
# input = sys.stdin.readline

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]

# minVal = 1e9
# def cal(c_rgb,depth,sum):
#     global minVal
#     if depth == n:
#         minVal = min(sum,minVal)
#         return
#     for i in range(3):
#         if i != c_rgb:
#             cal(i, depth+1,sum+board[depth][i])

# for i in range(3):
#     sum = 0
#     cal(i,0,sum)
# print(minVal)

import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

for i in range(1,len(board)):
    # R
    board[i][0] = min(board[i-1][1],board[i-1][2])+board[i][0]
    #G
    board[i][1] = min(board[i-1][0],board[i-1][2])+board[i][1]  
    # B
    board[i][2] = min(board[i-1][0],board[i-1][1])+board[i][2]

print(min(board[n-1]))