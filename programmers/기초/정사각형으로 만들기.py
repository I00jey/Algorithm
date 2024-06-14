def solution(arr):
    cols = len(arr[0])
    rows = len(arr)
    if cols >= rows:
        for i in range(cols - rows):
            arr.append([0] * cols)
    else:
        for i in range(rows):
            for j in range(rows - cols):
                arr[i].append(0)

    return arr


print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))

