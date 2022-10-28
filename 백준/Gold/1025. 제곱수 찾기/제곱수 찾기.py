import sys
import math
input = sys.stdin.readline
N, M = map(int, input().split())
 
board = [list(input())[:-1] for _ in range(N)]
answer = -1

def sqr(S): # 제곱수면 1 아니면 0
  S = int(S) 
  if math.sqrt(S)-int(math.sqrt(S))==0:
    return 1
  else:
      return 0


for i in range(N): 
    for j in range(M): 
      # 모든 좌표에 대해 -N~N/-M~M 범위 등차를 지정하여 반복문 실행
        for row_d in range(-N,N):
            for col_d in range(-M,M):
                S = ""
                x,y = i,j 
                if row_d == 0 and col_d == 0:
                    continue
                while 0 <= x < N and 0 <= y < M: #board 밖으로 벗어나지 않는 경우 
                    S += board[x][y] # 방문한 좌표의 숫자들을 이어 붙여줌
                    # 매 좌표마다 제곱수 판별 
                    if sqr(S): # 제곱수이면 
                        answer = max(answer,int(S))
                    # 시작 좌표부터 등차를 더해줌
                    x += row_d
                    y += col_d
print(answer)