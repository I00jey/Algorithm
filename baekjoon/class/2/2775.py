test_case = int(input())
for _ in range(test_case):
    k = int(input())
    n = int(input())
    people = 0
    apartment = [[1, 2, 3]]
    for i in range(k+1):
        apartment.append(sum([apartment[i][j] for j in range(n)]))
    print(people)
