def solution(genres, plays):
    answer = []
    # 장르별 총 재생 횟수와 노래 정보 저장
    # 장르별 총 재생 횟수 {장르: 총 재생 횟수}
    genre_plays = {}
    # 장르별 노래 정보 {장르: [(재생 횟수, 고유 번호), ...]}
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        # 장르별 총 재생 횟수 계산
        genre_plays[genre] = genre_plays.get(genre, 0) + play
        # 장르별 노래 정보 저장
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, i))

    # 장르를 총 재생 횟수 내림차순으로 정렬
    # 딕셔너리의 item()를 이용해 (키, 값) 쌍으로 얻고, 총 재생횟수를 기준으로 정렬
    sorted_genres = sorted(genre_plays.items(), key=lambda item: item[1], reverse=True)

    # 정렬된 장르 순서대로 노래 선택
    for genre, _ in sorted_genres:
        # 장르 내 노래들을 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬
        # 재생횟수는 음수로 변환하여 정렬
        sorted_songs = sorted(genre_songs[genre], key=lambda song: (-song[0], song[1]))
        # 각 장르에서 최대 2곡까지 추가
        answer.extend([song[1] for song in sorted_songs[:2]])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))