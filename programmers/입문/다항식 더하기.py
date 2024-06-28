# 내 풀이
def solution(polynomial):
    answer_arr = []
    # 빈칸을 기준으로 나눠 배열에 저장
    blink_out = polynomial.split()
    # '+'를 뺀 나머지 배열
    plus_out = [i for i in blink_out if i != '+']
    # 숫자 문자열만 저장한 배열
    num_arr = [int(i) for i in plus_out if i.isdigit()]
    # 'x'인 문자열을 1로 저장한 배열 (계수가 1인 x)
    x_arr1 = [1 for i in plus_out if i == 'x']
    # 'x'의 계수가 1이 아닌 일차항의 계수를 저장한 배열
    x_arr2 = [int(i.replace("x", "")) for i in plus_out if 'x' in i and i != 'x']
    # 다항식에 있는 'x'의 총 계수를 구하기 위해 배열 합하기
    x_arr = x_arr1 + x_arr2
    if len(x_arr):
        if sum(x_arr) == 1:
            # 총 'x'의 계수가 1일 경우 'x' 배열에 넣기
            answer_arr.append('x')
        else:
            # 1이 아니면 '{계수}x' 문자열을 배열에 넣기
            answer_arr.append(f'{sum(x_arr)}x')
    # 상수항이 있을 경우
    if len(num_arr):
        # 숫자 문자열로 변환 후 배열에 넣기
        answer_arr.append(str(sum(num_arr)))
    # ' + ' 구분자로 배열 요소를 문자열로 합치기
    #  만약 반환 배열에 아무것도 없다면 빈 문자열 반환
    return ' + '.join(answer_arr) if len(answer_arr) else ''


# 테스트 케이스
print(solution('x + x + x'))
print(solution('5 + 5 + x'))


# 다른 풀이
def solution(polynomial):
    xnum = 0
    const = 0
    # ' + '을 기준으로 다항식을 자름
    for c in polynomial.split(' + '):
        # 문자열이 숫자일 경우
        if c.isdigit():
            const+=int(c)
        else:
            # 'x' 계수가 1일 경우 1을 더하고, 1이 아니라면 x앞의 계수 정수화 후 더하기
            xnum = xnum+1 if c == 'x' else xnum+int(c[:-1])

    # 총 'x'의 계수가 0이라면
    if xnum == 0:
        # 상수항만 반환
        return str(const)
    # 1이라면
    elif xnum == 1:
        # 상수항이 없다면 'x'만 반환
        # 상수항이 있다면 'x + 상수항' 반환
        return 'x + '+str(const) if const != 0 else 'x'
    else:
        # 총 'x'의 계수가 2 이상
        # 상수항이 없다면 '{계수}x' 반환
        # 상수항이 있다면 '{계수}x + 상수항' 반환
        return f'{xnum}x + {const}' if const != 0 else f'{xnum}x'
