import sys 
input = sys.stdin.readline

T = int(input())
for t in range(T):
    mon, mdays, wdays = map(int,input().split())
    pointer = 0
    day =1
    line = 1
    for _ in range(mon*mdays-1):
        if day == mdays:
            if pointer == wdays-1:
                pointer = 0
            else:
                pointer+=1
            day = 1
            line+=1
        else:
            if pointer == wdays-1:
                pointer = 0
                line+=1
            else:
                pointer+=1
            day+=1
    print("Case #{}: {}".format(t+1, line))