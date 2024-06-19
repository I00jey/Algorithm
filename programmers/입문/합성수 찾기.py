def solution(n):
    answer = 0
    i = 1
    while i <= n:
        arr = [j for j in range(1, i+1) if i%j==0]
        if len(arr) >= 3:
            answer += 1
        i += 1
    return answer
