lis = []
for i in range(9):
    n = int(input())
    lis.append(n)

print(max(lis))
print(lis.index(max(lis))+1)