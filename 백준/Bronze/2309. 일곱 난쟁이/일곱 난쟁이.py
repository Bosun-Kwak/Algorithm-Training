from itertools import combinations

lst = []
for _ in range(9):
    lst.append(int(input()))
lst.sort()
res = combinations(lst,7)
r_lst = []
for r in res:
    sum = 0
    for i in range(7):
        sum += r[i]
    if sum == 100:
        r_lst = r
        break

for i in range(7):
    print(r[i])