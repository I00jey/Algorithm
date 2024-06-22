def solution(s):
    answer = ''
    arr = [i for i in s if s.count(i) == 1]
    return ''.join(sorted(arr))

