def solution(s):
    input_list = list(s)
    start = 0
    end = start+1
    print(input_list)
    result = ""
    length = 1
    while(end < len(input_list)):
        if input_list[start] == input_list[end]:
            print(input_list[start], input_list[end])
            end += 1
            length += 1
        elif input_list[start] != input_list[end] or end == len(input_list)-1:
            print(length)
            result += str(length)
            result += input_list[start]
            start = end
            end = start+1
            length = 1

    print(result)
    answer = 0
    return answer

solution("aabbaccc")