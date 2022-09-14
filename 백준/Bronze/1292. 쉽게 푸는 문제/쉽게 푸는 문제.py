import sys
input = sys.stdin.readline

a,b = map(int,input().split())

check = 0
check_a = 0
check_a_sum = 0
check_b = 0
check_b_sum = 0
a -=1
for i in range(1,1001):
  check+=i
  if a <= check:
    check_a = i
    check_a_sum = check
    break
  i+=1

check = 0
for i in range(1,1001):
  check+=i
  if b <= check:
    check_b = i
    check_b_sum = check
    break
  i+=1
  
sum_a = 0
for i in range(check_a):
  sum_a = sum_a + i*i
sum_a = sum_a + (check_a-(check_a_sum-a))*check_a
# print(sum_a)

sum_b = 0
# print(check_b)
for i in range(check_b):
  sum_b = sum_b + i*i
sum_b = sum_b + (check_b-(check_b_sum-b))*check_b

# print(sum_b)
print(sum_b-sum_a)