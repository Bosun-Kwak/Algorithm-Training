import sys
input = sys.stdin.readline

n = int(input())
S = [list(map(int,input().split())) for _ in range(n)]

# n = 4
# S = [[0,1,2,3],[4,0,5,6],[7,1,0,2],[3,4,5,0]]

visited = [0]*n
visited[0] = 1
min_val = 200

def startlink(cur,depth):
  start = 0
  link = 0
  global min_val

  if depth == n//2:
    # print(visited)
    for i in range(n):
      for j in range(n):
        if visited[i] ==1 and visited[j] == 1:
          start += S[i][j]
        elif visited[i] ==0 and visited[j] == 0:
          link += S[i][j]
    # print(start-link)
    min_val = min(min_val, abs(start-link))
    return
    
  for i in range(cur,n):
    if not visited[i]:
      visited[i] = 1
      startlink(i+1,depth+1)
      visited[i] = 0

startlink(1,1)
print(min_val)