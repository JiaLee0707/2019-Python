##연도가 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않는다.##
##400으로 나누어 떨어지는 연도는 윤년이다##
year = int(input("연도를 입력하시오 : "))
if ((year % 4 == 0 and year % 100 != 0) or (year % 4 == 0)):
    print("%d 년은 윤년입니다." % year)
else:
    print("%d 년은 윤년이 아닙니다." % year)
    
