# 스택큐

n = int(input())
stack = []

for i in range(n):
    string = input()
    str_list = string.split()
    if str_list[0] == 'push':
        stack.append(int(str_list[1]))
    elif str_list[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif str_list[0] == 'size':
        print(len(stack))
    elif str_list[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif str_list[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
