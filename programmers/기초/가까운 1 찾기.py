def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1


# 다른 풀이
# def solution(arr, idx):
#     answer = 0
#     try:
#         answer = arr.index(1, idx)
#     except:
#         answer = -1
#
#     return answer


print(solution([0, 0, 0, 1], 1))
print(solution([1, 0, 0, 1, 0, 0], 4))
print(solution([1, 1, 1, 1, 0], 3))


# index() 함수
# 시퀀스에서 특정 값의 첫 번째 발생 위치를 찾아서 해당 인덱스를 반환
# 대상값이 시퀀스 내에 없으면 ValueError 예외 발생

# 시작 인덱스와 종료 인덱스를 지정할 수 있는 매개변수 지원
# .index('str', 5)
#  인덱스 값 5부터 시작해서 'str' 문자열의 인덱스 찾기
# .index('a', 4, 6)
#  인덱스 값 4부터 6까지의 'a' 문자 인덱스 찾기

# 대상 값이 시퀀스에 없으면 에러가 발생하므로 <try-except> 블록 사용
# try:
#     index = s.index('x')
# except ValueError as e:
#     print(f"Error: {e}")  # 출력: Error: substring not found