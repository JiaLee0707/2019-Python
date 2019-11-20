c500, c100, c10 = 0, 0, 0

InputMoney = int(input("투입한 돈 : "))
OutMoney = int(input("물건값 : "))

giveMoney = InputMoney - OutMoney
c500 = giveMoney // 500
giveMoney = giveMoney % 500
c100 = giveMoney // 100
giveMoney = giveMoney % 100
c10 = giveMoney // 10

print("\n 거스름돈 : %d" % giveMoney)
print("\n 500원 동전의 개수 : %d" % c500)
print("\n 100원 동전의 개수 : %d" % c100)
print("\n 10원 동전의 개수 : %d" % c10)
