## 변수 선언 부분 ##
money, c50000, c10000, c5000, c1000 = 0, 0, 0, 0, 0


## 메인 코드 부분 ##
money = int(input("교환할 돈은 얼마?"))

c50000 = money // 50000
money %= 50000

c10000 = money // 10000
money %= 10000

c5000 = money // 5000
money %= 5000

c1000 = money // 1000
money %= 1000

print("\n 50000원 짜리 ==> %d개" % c50000)
print("\n 10000원 짜리 ==> %d개" % c10000)
print("\n 5000원 짜리 ==> %d개" % c5000)
print("\n 1000원 짜리 ==> %d개" % c1000)
print("\n 바꾸지 못한 잔돈 ==> %d원" % money)
