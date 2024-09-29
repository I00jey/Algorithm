# 입력할 단어 개수
n = int(input())
# 단어 저장할 디렉토리
strings = {}

for i in range(n):
    word = input()
    # 입력한 단어의 길이가 기존 단어 길이와 같을 때
    if len(word) in strings:
        # 입력 단어가 기존 단어와 일치하다면
        if word in strings[len(word)]:
            # 저장없이 다음 입력으로
            continue
        # 일치하는 기존 단어가 없다면
        else:
            # 단어길이가 키인 디렉토리 값(배열)에 입력단어 넣기
            strings[len(word)].append(word)
    else:
        # 기존 단어와 길이가 일치하지 않다면 배열 초기화
        strings[len(word)] = [word]


# 범위 0부터 단어 길이의 최대 값까지
for j in range(max(strings)+1):
    # j에 해당하는 단어길이가 있다면
    if j in strings:
        # 같은 길이를 가진 단어를 사전순으로 출력
        for word in sorted(strings[j]):
            print(word)
