n, m = map(int, input().split())

slist = []
for i in range(n):
    slist.append(input())

slist.sort()

dna = ''
# n: 주어지는 문자열 갯수
# m: 문자열의 길이
for y in range(m):
    ATGC = {'A':0, 'C':0, 'G':0, 'T':0}
    for x in range(n):
        ATGC[slist[x][y]] += 1
    dna += max(ATGC, key=ATGC.get)

total_hd = 0
for x in range(n):
    for y in range(m):
        if dna[y] != slist[x][y]:
            total_hd += 1

print(dna)
print(total_hd)