def solution(todo_list, finished):
    return [list for idx, list in enumerate(todo_list) if finished[idx] == False]


print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"],
               [True, False, True, False]))