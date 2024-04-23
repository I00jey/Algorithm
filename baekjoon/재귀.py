# from itertools import combinations
#
# def combination_boj_6603():
#     while True:
#         num_array = []
#         input_list = list(map(int, input().split()))
#         k = input_list[0]
#         if k == 0:
#             break
#         for i in range(1, len(input_list)):
#             num_array.append(input_list[i])
#         comb = combinations(num_array, 6)
#         for i in comb:
#             print(*i)
#         print()
#
# combination_boj_6603()


# -------------팩토리얼----------------
# def fect(index):
#     if index == 1:
#         return 1
#     return fect(index-1) * index
# print(fect(4))

# -------------피보나치 수열-------------
# def func(index):
#     if index <= 2:
#         return 1
#     else:
#         return func(index-1) + func(index-2)
#
# print(func(7))