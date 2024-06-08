def solution(arr, n):
    if len(arr) % 2:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n
    return arr

# range(시작, 끝(미포함), 스텝(스킵 칸수))