from collections import deque

n = int(input())

a = deque([i+1 for i in range(n)])

while True:
    if len(a) == 1:
        print(a[0])
        break
    a.popleft()
    a.rotate(-1)

