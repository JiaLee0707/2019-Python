import random

print("동전 던지기 게임을 시작합니다.")

# randrange(2) : 0~1 사이의 값을 리턴
coin = random.randrange(2)
if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
    
print("게임이 종료되었습니다.")
