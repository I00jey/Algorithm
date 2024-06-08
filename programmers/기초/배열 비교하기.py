# 내 풀이
def solution(arr1, arr2):
    answer = 0
    if len(arr1) != len(arr2):
        if len(arr1) == max(len(arr1), len(arr2)):
            answer = 1
        else:
            answer = -1

    else:
        if sum(arr1) == sum(arr2):
            answer = 0
        elif sum(arr1) == max(sum(arr1), sum(arr2)):
            answer = 1
        else:
            answer = -1
    return answer

# 다른 풀이
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
#   arr1 > arr2 경우
#   True - False = 1 - 0 = 1
#   or 이니까 하나만 1이여도 1