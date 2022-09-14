import sys
input =  sys.stdin.readline
N,K = map(int, input().split())

num_list = []
for i in range(1, N+1):
  if N%i == 0:
    num_list.append(i)

# print(num_list)

if len(num_list) <K:
  print("0")
else:
  print(num_list[K-1])