i, j = 0, 0

# 별 모양의 글자 출력하는 코드
# print('\u2605')


while i < 9:
    while j < i:
        print('\u2605 ')
        j += 1
    i += 1
    j = 0
    print('')
