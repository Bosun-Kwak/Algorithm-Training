import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(n-1,0,-1):
    if nums[i]>nums[i-1]:
        for j in range(n-1,0,-1):
            if nums[j]>nums[i-1]:
                nums[j],nums[i-1] = nums[i-1],nums[j]
                cnt =1
                break
    if cnt == 1:
        nums = nums[:i]+sorted(nums[i:])
        print(*nums)
        break
if cnt == 0:
    print("-1")


'''
1. itertools 바로 쓰려고 하지 말기 -> 시간 초과 
2. 예시 잘 생각해서 풀기 
3. 출력 형태 check 

'''
