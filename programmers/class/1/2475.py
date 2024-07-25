lis = map(int, input().split())
print((sum(pow(i, 2) for i in lis)) % 10)