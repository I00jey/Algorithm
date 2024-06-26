# 내 풀이 (테스트 케이스 통과 / 정확성 29.4)
def solution(quiz):
    answer = []
    for i in quiz:
        arr1 = i.split("=")
        quiz_sum = int(arr1[1])
        quiz_nums = [int(i.replace(" ", "")) for i in arr1[0].replace("-","+-").split("+")]
        if quiz_sum == sum(quiz_nums):
            answer.append("O")
        else:
            answer.append("X")
    return answer

# 내 풀이2 (테스트 케이스 통과 / 정확성 41.2)
def solution2(quiz):
    answer = []
    for i in quiz:
        left, right = i.split("=")
        quiz_sum = int(right.strip())
        total = 0
        nums = left.replace(" - ", " + - ").split(" + ")
        for num in nums:
            num = num.strip()
            num = num.replace(" ", "")
            total += int(num)
        if total == quiz_sum:
            answer.append("O")
        else:
            answer.append("X")
    return answer


# 내 풀이3 (테스트 케이스 통과 / 정확성 41.2)
def solution3(quiz):
    answer = []
    for i in quiz:
        left, right = i.split("=")
        quiz_sum = int(right.strip())
        total = 0
        nums = left.replace(" - ", " + -").split(" + ")
        for num in nums:
            total += int(num)
        if total == quiz_sum:
            answer.append("O")
        else:
            answer.append("X")
    return answer


# 내 풀이4 (테스트 케이스 통과 / 정확성 41.2)
def solution4(quiz):
    answer = []
    for i in quiz:
        left, right = i.split(" = ")
        quiz_sum = int(right.strip())
        nums = left.replace(" - ", "+-").split("+")
        total = 0
        for num in nums:
            total += int(num)
        if total == quiz_sum:
            answer.append("O")
        else:
            answer.append("X")
    return answer


# 내 풀이5 (테스트 케이스 통과 / 정확도 100.0)
def solution5(quiz):
    answer = []
    for q in quiz:
        total = q.split()
        quiz_result = int(total[-1])
        if total[1] == '+':
            if quiz_result == int(total[0]) + int(total[2]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if quiz_result == int(total[0]) - int(total[2]):
                answer.append("O")
            else:
                answer.append("X")
    return answer


# 다른 풀이 1 (eval 함수 사용)
def valid(equation):
    equation = equation.replace('=', '==')
    # 수식에서 '='를 '=='로 변경
    return eval(equation)
    # eval 함수를 통해 문자열을 파이썬 코드로 수행
    # True 또는 False 반환

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]
    # valid 함수의 반환값에 따라 리스트에 "O" 또는 "X" 저장



# 다른 풀이 2
def solution(quiz):
    answer = []
    for q in quiz:
        L,R = q.split(' = ')
        # ' = '을 기준으로 연산식과 값 나누기
        a,op,b = L.split()
        # split()을 통해 연산식을 연산자와 피연산자로 분해
        if op=='+':
            result = 'O' if int(a)+int(b)==int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b)==int(R) else 'X'
            answer.append(result)
    return answer

print(solution5(["3 - 4 = -3", "5 + 6 = 11"]))

