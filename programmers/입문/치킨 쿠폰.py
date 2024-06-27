# 내 풀이
def solution(chicken):
    count = 0
    while chicken > 9:
        count += chicken//10
        # 치킨 수(쿠폰 수)를 10으로 나눠 서비스 치킨 수 더하기
        chicken = chicken//10 + chicken % 10
        # 서비스 치킨을 시키고 남은 나머지 쿠폰 수랑 서비스 치킨으로 받은 쿠폰 수 더하기
    return count

