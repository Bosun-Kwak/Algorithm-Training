cnt = 0

def dfs(cur, res, numbers, target):
    global cnt
    if cur == len(numbers):
        if res == target:
            cnt += 1
        return
    # +
    dfs(cur+1, res+numbers[cur],numbers, target)
    # - 
    dfs(cur+1, res-numbers[cur],numbers, target)  

def solution(numbers, target):
    dfs(0,0,numbers, target)
    return cnt