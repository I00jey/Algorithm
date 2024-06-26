def solution(id_pw, db):
    answer = ''
    # id가 db의 id 배열에 있을 경우
    if id_pw[0] in [i[0] for i in db]:
        for j in range(len(db)):
            # 입력한 로그인 정보(리스트)와 db 정보(리스트)가 일치할 경우
            if id_pw == db[j]:
                answer = "login"
                break
                # 로그인 여부를 확인했으니 반복문 종료
            else:
                # db에 아이디를 존재하지만 비밀번호까지 일치하지 않을 경우
                answer = "wrong pw"
    else:
    # id가 db의 id 배열에 없을 경우
        answer = 'fail'
    return answer