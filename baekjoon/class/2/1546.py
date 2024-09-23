n = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
sum_score = 0
for i in score_list:
    # 새로운 평균 계산법
    # 최고점 과목을 포함한 모든 과목의 점수를 바꿈
    sum_score += i/max_score*100

print(sum_score/n)