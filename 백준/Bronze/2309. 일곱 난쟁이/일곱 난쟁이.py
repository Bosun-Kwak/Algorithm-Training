import sys
input = sys.stdin.readline

num_list =[]
for i in range(9):
  num_list.append(int(input()))

# num_list = [20,7,23,19,10,15,25,8,13]
num_list.sort()
sum = sum(num_list[:])
# print(sum)


for i in range(8):
  for j in range(i+1,9):
    sum2 = sum
    sum2 = sum2 - num_list[i]-num_list[j]
    if sum2 == 100:
      # num_list.remove(num_list[i])
      # num_list.remove(num_list[j-1])
      no_1 = i
      no_2 = j
      break

for i in range(9):
  if i != no_1 and i != no_2:
    print(num_list[i])