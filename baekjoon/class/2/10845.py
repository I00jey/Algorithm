# 큐
from collections import deque
import sys

# 시간 제한 때문에 sys.stdin.readline() 사용
n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    string = sys.stdin.readline()
    lis = string.split()

    # if lis[0] == 'push':
    #     queue.append(lis[1])
    # elif lis[0] == 'pop':
    #     if len(queue) == 0:
    #         print(-1)
    #     else:
    #         print(queue.popleft())
    # elif lis[0] == 'size':
    #     print(len(queue))
    # elif lis[0] == 'empty':
    #     if len(queue) == 0:
    #         print(1)
    #     else:
    #         print(0)
    # elif lis[0] == 'front':
    #     if len(queue) == 0:
    #         print(-1)
    #     else:
    #         print(queue[0])
    # elif lis[0] == 'back':
    #     if len(queue) == 0:
    #         print(-1)
    #     else:
    #         print(queue[-1])
    if lis[0] == 'push':
        queue.append(lis[1])
    elif lis[0] == 'size':
        print(len(queue))
    elif lis[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    else:
        if len(queue) == 0:
            print(-1)
        else:
            if lis[0] == 'pop':
                print(queue.popleft())
            elif lis[0] == 'front':
                print(queue[0])
            elif lis[0] == 'back':
                print(queue[-1])