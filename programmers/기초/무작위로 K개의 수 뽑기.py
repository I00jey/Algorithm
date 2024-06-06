# 내 풀이
def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    return answer[:k] if not len(answer) < k else answer + [-1]*(k-len(answer))
    # 굳이 if문을 쓰지 않아도 answer 길이와 k가 같으면 -1 추가 안됨
    # return answer + [-1]*(k-len(answer))

# 다른 풀이
def solution(arr, k):
    res = list(dict.fromkeys(arr))
    res.extend([-1] * (k - len(res)))
    return res[:k]

# dict.fromkeys(iterable, value=None)
# 파이썬의 딕셔너리 메소드
# 주어진 키들을 사용해서 새로운 딕셔너리 생성
# value는 생략할 경우 기본값 None



print(solution([0, 1, 1, 2, 2, 3], 3))
print(solution([0, 1, 1, 1, 1], 4))