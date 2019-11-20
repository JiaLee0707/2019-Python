##정수를 입력받아 양수인지, 0인지, 음수인지를 구별하는 프로그램##
num = int(input("정수를 입력하시오 : "))

## if~elif~else 구문 ##
'''
if num > 0:
    print("%d는 양수입니다." % num)
elif num < 0:
    print("%d는 음수입니다." % num)
else :
    print("0입니다.")
'''

## 중첩if문 ##
if num >= 0:
    if num == 0:
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")
