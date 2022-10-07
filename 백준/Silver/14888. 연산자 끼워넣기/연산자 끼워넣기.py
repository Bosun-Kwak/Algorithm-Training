import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multip, div):
  global maximum, minimum
  
  if depth == N:
    maximum = max(total, maximum)
    minimum = min(total, minimum)
    return 

  if plus:
    dfs(depth+1, total+A[depth], plus-1, minus, multip, div)
  if minus:
    dfs(depth+1, total-A[depth], plus, minus-1, multip, div)
  if multip:
    dfs(depth+1, total*A[depth], plus, minus, multip-1, div)
  if div:
    dfs(depth+1, int(total/A[depth]), plus, minus, multip, div-1)

dfs(1,A[0],op[0],op[1],op[2],op[3])
print(maximum)
print(minimum)
