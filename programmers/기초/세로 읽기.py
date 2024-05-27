def solution(my_string, m, c):
    my_arr = []
    arr = []
    for idx, word in enumerate(my_string):
        arr.append(word)
        if (idx+1) % m == 0:
            my_arr.append(arr)
            arr = []
    return ''.join([my_arr[i][c-1] for i in range((len(my_string)//m))])
    # 문제에서 세로로 c번째에 적힌 글자들을 출력하라고 했으니까 인덱스는 c-1

# 다른 풀이
def solution(s, m, c):
    return s[c-1::m]
# c-1 인덱스부터 문자열 끝까지 m만큼 넘기며 슬라이싱

print(solution("ihrhbakrfpndopljhygc",4,2))
print(solution("programmers",1,1))