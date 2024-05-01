def solution(n, control):
    for i in control:
        if i == "w": n += 1
        elif i == "s": n -= 1
        elif i == "d": n += 10
        elif i == "a" : n -= 10
    return n

# 다른 풀이
# def solution(n, control):
#   key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
#   return n + sum([key[c] for c in control])

# zip(반복 가능한 객체 iterable)
# : 여러 개의 iterable 를 인자로 받아 각 iterable 에서 동일한 인덱스의 요소들을 묶어서 튜플로 변환
# zip([a,b,c], [1,2,3]) => [(a,1), (b,2), (c,3)]
# print(list(zip([1,2,3],[4,5,6],[7,8,9])))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# dict(key-value 쌍)
# 여러 개의 key-value 쌍을 인자로 받아서 딕셔너리로 변환
# print(dict(zip([1,2,3],[4,5,6])))
# 1: 4, 2: 5, 3: 6}

print(solution(0,"wsdawsdassw"))

