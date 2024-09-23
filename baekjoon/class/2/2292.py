n = int(input())
box_number = 1
count = 1

# 입력받은 박스값이 다음 칸의 최댓값보다 작을 경우 반복
while n > box_number:
    box_number += 6 * count
    count += 1
print(count)

# 칸은 6의 배수만큼 시계방향으로 증가
# 1
# 1 + 6*1 -> 7
# 7 + 6*2 -> 19
# ...

