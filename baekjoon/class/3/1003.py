# 피보나치 함수



t = int(input())
# 출력 횟수 저장
fibo_print_list = [[0, 0] for _ in range(t)]
for i in range(t):

    def fibonacci(n):
        if n == 0:
            print("0")
            return 0
        elif n == 1:
            print("1")
            return 1
        else:
            return fibonacci(n‐1) + fibonacci(n‐2)
