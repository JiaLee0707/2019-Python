aa = [0, 0, 0, 0]
hap = 0

i = 0
while(i < 4):
    aa[i] = int(input("%d번째 숫자 : " %(i+1)))
    hap = hap + aa[i]
    i += 1

print("합계 ==> %d" % hap)
