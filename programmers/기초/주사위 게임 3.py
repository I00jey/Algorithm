def solution(a, b, c, d):
    answer = 0
    arr = [a,b,c,d]
    set_arr = list(set(arr))
    print(set_arr)
    if len(set_arr) == 1:
        answer = 1111 * set_arr[0]
    elif len(set_arr) == 2:
        if arr.count(set_arr[0]) == 1:
            answer = pow(10*set_arr[1]+set_arr[0], 2)
        elif arr.count(set_arr[0]) == 2:
            answer = abs(set_arr[0]-set_arr[1])*(set_arr[0]+set_arr[1])
        else:
            answer = pow(10 * set_arr[0] + set_arr[1], 2)
    elif len(set_arr) == 3:
        answer = 1
        for i in set_arr:
            if arr.count(i) == 1:
                answer *= i
    else:
        answer = min(arr)
    return answer


# 다른 풀이
def solution(a, b, c, d):
    # 주사위 숫자 배열
    l = [a,b,c,d]
    # 주사위 숫자 카운트 배열
    c = [l.count(x) for x in l]
    # 같은 숫자가 4번 나왔을 때
    if max(c) == 4:
        return 1111*a
    # 같은 숫자가 3번 나왔을 때
    elif max(c) == 3:
        # c.index(3) => c 배열에서 3 값을 가지고 있는 인덱스
        return (10*l[c.index(3)]+l[c.index(1)])**2
    # 같은 숫자가 2번 나왔을 때
    elif max(c) == 2:
        # 같은 숫자 2개가 1쌍일 때
        if min(c) == 1:
            # 카운트가 1인 요소만 골라서 곱하기
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        # 같은 숫자 2개가 2쌍일 때
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)

print(solution(2,2,2,2))
print(solution(4,1,4,4))
print(solution(6,3,3,6))
print(solution(2, 5, 2, 6))
print(solution(6,4,2,5))