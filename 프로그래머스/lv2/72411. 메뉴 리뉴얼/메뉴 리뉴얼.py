from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        check = []
        for o in orders:
            o_list = list(o)
            o_list.sort()
            if len(o)<c:
                pass
            check += list(combinations(o_list,c))
        check.sort()
        if len(check)==0:
            break
        cnt = check.count(check[0])
        max = cnt
        max_value=[check[0]]
        for i in range(cnt,len(check)):
            if i!=0 and check[i]!= check[i-1]:
                cnt = check.count(check[i])
                if max<cnt :
                    max = cnt
                    max_value = []
                    max_value.append(check[i])
                elif max==cnt:
                    max_value.append(check[i])

        for m in max_value:
            if max!=1:
                str = ''.join(m)
                answer.append(str)
    answer.sort()
        
    return answer