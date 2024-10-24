# 비밀번호 찾기

n, m = map(int, input().split())

login_dict = {}

for _ in range(n):
    web, pw = input().split()
    login_dict[web] = pw

for _ in range(m):
    input_web = input()
    print(login_dict[input_web])