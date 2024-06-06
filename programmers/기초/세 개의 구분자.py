# 내 풀이
def solution(myStr):
    str1 = myStr.replace("a", ",").replace("b", ",").replace("c", ",")
    arr = [i for i in str1.split(",") if i]
    return ["EMPTY"] if len(arr) == 0 else arr


print(solution("baconlettucetomato"))
print(solution("abcd"))
print("cabab")