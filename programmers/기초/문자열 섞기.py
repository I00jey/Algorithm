def solution(str1, str2):
    # 내 풀이
    answer = ''
    for i in range(len(str1)):
        answer += (str1[i]+str2[i])
    return answer

    # 다른 풀이
    # answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    # [] 대괄호 안에서 for문을 돌려 str1[i]+str2[i]가 각 요소인 리스트 완성

    # ''.join(리스트)
    # 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 변환하는 함수
    # '구분자'.join(리스트)
    # 리스트의 값과 값 사이에 구분자를 넣어서 하나의 문자열로 합침


print(solution("aaaaa", "bbbbb"))
