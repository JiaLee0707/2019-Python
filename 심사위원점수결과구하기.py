## 심사위원 점수 결과 구하기 ##

## 점수 리스트 생성
scores = []

print("5명의 평가 점수를 입력하세요!(100점 만점)")

# 변수 초기화
count = 0
max_score = 0
min_score = 100

while count < 5:
    score = int(input("점수 입력 : "))
    scores.append(score)

    # 최대값 저장
    if max_score < score:
        max_score = score

    # 최소값 저장
    if min_score > score :
        min_score = score

    count += 1

print("\n##총 입력 점수##")

for item in scores:
    print(item, "점")

print("\n##제거 대상 점수##")
print("- 최고 점수 : ", max_score , "점")
print("- 최소 점수 : " , min_score , "점")

scores.remove(max_score)
scores.remove(min_score)

print("\n##최정 입력 점수##")

total = 0
for item in scores:
    print(item, "점")
    total += item

avg = round(total / len(scores), 2)

print("----------")
print("- 총점 : " , total , "점")
print("- 평균: " , avg , "점")
