def solution(n):
    arr = sorted(list(str(n)), reverse=True)
    answer = ''.join(arr)
    return int(answer)

solution(118372)