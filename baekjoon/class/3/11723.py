# 집합

# input() 사용 시, 시간 초과
# sys.stdin.readline 사용
import sys
input = sys.stdin.readline

# 연산 수
m = int(input())

# 집합 초기화
s = set()

for i in range(m):
    string = input().split()
    operation = string[0]
    if len(string) > 1:
        num = int(string[1])
        if operation == 'add' and num not in s:
            s.add(num)
        elif operation == 'remove' and num in s:
            s.remove(num)
        elif operation == 'check':
            print(int(bool(num in s)))
        elif operation == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)
    else:
        if operation == 'all':
            s.update(i for i in range(1, 21))
        elif operation == 'empty':
            s.clear()
