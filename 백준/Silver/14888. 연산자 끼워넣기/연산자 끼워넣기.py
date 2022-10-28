import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_r = -1e9
min_r = 1e9
def cal(plus, minus, mul, div,i,res):
    global max_r, min_r
    if i==n:
        # print("res: {}".format(res))
        max_r = max(res,max_r)
        min_r = min(res,min_r)
        return 
    if plus:
        cal(plus-1,minus, mul,div,i+1,res+A[i])
    if minus:
        cal(plus,minus-1, mul,div,i+1,res-A[i])
    if mul:
        cal(plus,minus, mul-1,div,i+1,res*A[i])
    if div:
        cal(plus,minus,mul,div-1,i+1,int(res/A[i]))

cal(plus, minus, mul, div,1,A[0])
print(max_r)
print(min_r)