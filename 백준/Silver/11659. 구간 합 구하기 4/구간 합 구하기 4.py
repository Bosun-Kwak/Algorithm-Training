import sys
input =  sys.stdin.readline
N,M = map(int, input().split())

data = list(map(int,input().split()))
sum_list = data

# 누적합
for i in range(N-1):
  sum_list[i+1] += sum_list[i]

  
  
for i in range(M):
  start,end = map(int, input().split())
  if start != 1:
    print(sum_list[end-1]-sum_list[start-2])
  else:
    print(sum_list[end-1])