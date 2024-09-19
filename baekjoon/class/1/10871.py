n, x = map(int, input().split())
lis = map(int, input().split())
print(' '.join([str(i) for i in lis if i < x]))