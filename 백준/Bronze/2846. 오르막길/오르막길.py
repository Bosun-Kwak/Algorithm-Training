import sys
input = sys.stdin.readline

n= int(input())
line = list(map(int,input().split()))

maxl = 0
cnt= 0
for i in range(1, len(line)):
    if line[i-1]<line[i]:
        cnt += (line[i]-line[i-1])
    else:
        cnt = 0
    if cnt>maxl:
        maxl = cnt
print(maxl)
        