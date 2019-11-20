dice1, dice2, dice3, dice4, dice5, dice6 = [0]*6
throwCount = 0

## 메인 코드 부분 ##
while True:
    throwCount += 1

    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    dice3 = random.randrange(1,7)
    dice4 = random.randrange(1,7)
    dice5 = random.randrange(1,7)
    dice6 = random.randrange(1,7)

    if dice1 == dice2 == dice3 == dice4 == dice5 == dice6:
        print('6개의 주사위가 모두 동일한 숫자가 나옴 -->',
              dice1, dice2, dice3, dice4, dice5, dice6)
        break;

print('6개가 동일한 숫자가 나올 때까지 \
      사위를 던진 횟수 : ' throwCount)
