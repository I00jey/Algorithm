a, b, v = map(int, input().split())

day = (v-b) // (a-b)
# v-b 목표 높이 v에 도달하는 날은 밤에 내려가지 않기 때문 & 낮 동안의 상승만 고려
# 밤에 안 내려가니까 미리 v에서 빼기

if (v - b) % (a - b) != 0:
    day += 1


print(day)