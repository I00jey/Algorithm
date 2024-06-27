def solution(polynomial):
    answer_arr = []
    blink_out = polynomial.split()
    plus_out = [i for i in blink_out if i != '+']
    num_arr = [int(i) for i in plus_out if i.isdigit()]
    x_arr1 = [1 for i in plus_out if i == 'x']
    x_arr2 = [int(i.replace("x", "")) for i in plus_out if 'x' in i and i != 'x']
    x_arr = x_arr1 + x_arr2
    if len(x_arr):
        if sum(x_arr) == 1:
            answer_arr.append('x')
        else:
            answer_arr.append(f'{sum(x_arr)}x')
    if len(num_arr):
        answer_arr.append(str(sum(num_arr)))
    return ' + '.join(answer_arr) if len(answer_arr) else ''


print(solution('x + x + x'))
print(solution('5 + 5 + x'))