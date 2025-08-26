from collections import Counter
def solution(participant, completion):
    answer = ''
    cnt_participant = Counter(participant)
    cnt_completion = Counter(completion)
    answer = (cnt_participant - cnt_completion).most_common(1)[0][0]
    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
