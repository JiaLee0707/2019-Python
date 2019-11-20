import random

## 변수 선언 ##
A, B
count=0

while True:
    count += 1
    A = random.randrange(1,7)
    B = random.randrange(1,7)


print("총 %d번 던져 주사위 A와 B가 같아졌습습니다."%count)
