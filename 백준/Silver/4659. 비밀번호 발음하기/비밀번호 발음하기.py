import sys
input = sys.stdin.readline

while True:
    v_cnt = 0 # 모음 개수
    con_c = 0 # 연속 자음 개수  (3개일 때 걸러내기)
    con_v = 0 # 연속 모음 개수 (3개일 때 걸러내기)
    res = 1
    # Try #1 /n 제거 방식 바꾸기 
    test = input().rstrip()
    if test == 'end':
        break
    
    for i in range(len(test)):
        if i> 0:
          if test[i] == test[i-1]:
              if test[i] != 'e' and test[i] != 'o':
                v_cnt = 0
                break
        
        if test[i] in 'aeiou':
            v_cnt +=1
            con_v +=1
            con_c = 0
            if con_v == 3:
                res = 0
                break
        else:
            con_v = 0
            con_c += 1
            if con_c == 3:
                res = 0
                break
        
# Try #2,#3 : print 방식 바꾸기
    if v_cnt == 0 or res ==0:
        print("<"+ test +"> is not acceptable.")

    else:
        print("<"+ test +"> is acceptable.")


