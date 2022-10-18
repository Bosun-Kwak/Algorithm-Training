n = int(input())
poporder = []
for _ in range(n):
    poporder.append(int(input()))
c = 1
# print(poporder)
stack = []
answer = []
# print(stack)
ansNo = 0
for p in poporder:
    while c<=p:
        stack.append(c)
        answer.append('+')
        c+=1
    if stack[-1] == p:
        stack.pop()
        answer.append('-')
    else:
        ansNo = 1
        break

if ansNo == 1:
    print("NO")
else:
    for a in answer:
        print(a)