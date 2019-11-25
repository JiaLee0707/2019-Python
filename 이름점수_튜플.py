import operator

count = int(input('입력하는 학생수가 총 몇명인가요? : '))
print('학생의 이름과 시험 점수를 차례대로 입력하세요!')

scores = list()
num = 1

# 이름 및 점수 입력
while num <= count :
    print(num, '번째 학생 =====')
    name = input('* 이름 : ')
    score = int(input('* 점수 : '))
    pair = (name, score) #튜플
    scores.append(pair) #리스트에 저장
    num += 1

# 딕셔너리로 타입 전환
scores_dict = dict(scores)

# 학생 이름 및 점수 출력
flag = True
while flag:
    wanted = input('어떤 학생의 점수가 궁금하신가요? 이름을 입력하세요 : ')

    if wanted in scores_dict :
        print(wanted, '학생의 점수 : ', scores_dict[wanted])
        flag = False
        print('검색 프로그램을 종료합니다.')
    else :
        print('찾는 학생(', wanted, ')의 점수가 존재하지 않습니다.')
        #print('찾는 학생(%s)의 점수가 존재하지 않습니다.' % wanted)

# 전체 학생의 이름 출력
print('전체 학생의 이름은 : ')
print(list(scores_dict.keys()))

#전체데이터를 튜플 형태로 출력
print('전체 데이터를 items() 로 출력 : ')
print(list(scores_dict.items()))
