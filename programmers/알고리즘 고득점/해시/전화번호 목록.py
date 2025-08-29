# 풀이 1
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for idx, value in enumerate(phone_book):
#         if idx+1 < len(phone_book) and phone_book[idx] == phone_book[idx+1][:len(phone_book[idx])]:
#             answer = False
#     return answer
# 시간복잡도: O(N log N) (정렬) + O(N) (인접 비교) = O(N log N)

# 풀이 2
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
# 조건 만족 즉시 리턴 → 평균 실행 속도 개선.

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))