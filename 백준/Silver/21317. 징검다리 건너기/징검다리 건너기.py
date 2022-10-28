import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for i in range(1,n):
    d[i] = list(map(int, input().split()))
k = int(input())
minV = 1e9
def cal(idx,sumV,bigjump):
    global minV
    
    # print("idx: {}, sumV: {}".format(idx,sumV))
    if idx == n:
        minV = min(sumV, minV)
        # print("@@@@@@@@@@@@@@@")
        # print("idx: {}, sumV: {}".format(idx,sumV))
        return 
    elif idx > n:
        return
    if bigjump == 0:
        cal(idx+3,sumV+k,1)
    # if (idx+1)<n:
    cal(idx+1, sumV+d[idx][0],bigjump)
    # if (idx+2)<n:
    cal(idx+2, sumV+d[idx][1],bigjump)
    

cal(1,0,0)
print(minV)

'''
실수 : 
1. 큰 jump의 의미를 파악X (문제 제대로 읽기)
2. k가 한번 주어지는거 (문제 제대로 읽기) 
3. "돌"에서 jump하는 에너지임 (나는 돌에 작은점프로 도착했을때, 큰 점프로 도착했을 때의 에너지로 파악함 )
'''
