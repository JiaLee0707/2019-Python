Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:/Users/User/Desktop/Python/Code03-01.py =============
123
  123
00123
123.450000
  123.5
123.450
Python
    Python
>>> 
============= RESTART: C:/Users/User/Desktop/Python/Code03-02.py =============

줄바꿈
연습

탭키	연습
글자가 "강조"되는 효과1
글자가 '강조'되는 효과2
\\\ 역슬래시 세 개 출력
\n \t \" \\를 그대로 출력
>>> 
============= RESTART: C:/Users/User/Desktop/Python/Code03-02.py =============

줄바꿈
연습
	탭키	연습
글자가 "강조"되는 효과1
글자가 '강조'되는 효과2
\\\ 역슬래시 세 개 출력
\n \t \" \\를 그대로 출력
>>> boolVar, intVar, floatVar, strVar = True, 0, 0.0, "strVar"
>>> boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""
>>> type(boolVar)
<class 'bool'>
>>> type(strVar)
<class 'str'>
>>> type(boolVar), type(intVar), type(floatVar), type(strVar)
(<class 'bool'>, <class 'int'>, <class 'float'>, <class 'str'>)
>>> boolVar = 100
>>> type(boolVar)
<class 'int'>
>>> 
============= RESTART: C:/Users/User/Desktop/Python/Code03-04.py =============
입력 진수 결정(16/10/8/2) : 16
값 입력 : 3333
16진수 ==>  0x3333
10진수 ==>  13107
 8진수 ==>  0o31463
 2진수 ==>  0b11001100110011
>>> a = 100 ** 100
>>> print(a)(
	)
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(a)(
TypeError: 'NoneType' object is not callable
>>> print(a)
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> a = (100 = 100)
SyntaxError: invalid syntax
>>> a = (100 == 100)
>>> b = (10 > 100)
>>> print(a, b)
True False
>>> a = "파이썬 만세"
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
'파이썬 만세'
>>> print(a
      )
파이썬 만세
>>> type(a)
<class 'str'>
>>> 
============== RESTART: C:/Users/User/Desktop/Python/ch3연습10.py ==============
16진수 한 글자 입력(0~9 a~f) : a
Traceback (most recent call last):
  File "C:/Users/User/Desktop/Python/ch3연습10.py", line 1, in <module>
    sel = int(input("16진수 한 글자 입력(0~9 a~f) : "))
ValueError: invalid literal for int() with base 10: 'a'
>>> 
=============== RESTART: C:/Users/User/Desktop/Python/ch310.py ===============
16진수 한 글자 입력(0~9 a~f) : a
10진수 ==>  10
>>> 
=============== RESTART: C:/Users/User/Desktop/Python/ch310.py ===============
16진수 한 글자 입력(0~9 a~f) : f
10진수 ==>  15
>>> 
============== RESTART: C:/Users/User/Desktop/Python/ch3연습10.py ==============
16진수 한 글자 입력(0~9 a~f) : a
10진수 ==>  10
>>> 
===================== RESTART: E:/Python/ch3name_age.py =====================
이름을 입력하세요 : 홍길동
나이를 입력하세요 : 30
이름은 %s, 나이는 %d 입니다. 홍길동 30
>>> 
===================== RESTART: E:/Python/ch3name_age.py =====================
>>> 
이름을 입력하세요 : 홍길동
나이를 입력하세요 : 30
Traceback (most recent call last):
  File "E:/Python/ch3name_age.py", line 3, in <module>
    print("이름은 %s, 나이는 %d 입니다." % (name, age))
TypeError: %d format: a number is required, not str
>>> 
===================== RESTART: E:/Python/ch3name_age.py =====================
이름을 입력하세요 : 홍길동
나이를 입력하세요 : 30
이름은 홍길동, 나이는 30 입니다.
>>> 
===================== RESTART: E:/Python/ch3name_age.py =====================
이름을 입력하세요 : 홍길동
나이를 입력하세요 : 30
이름은 홍길동, 나이는 30 입니다.
>>> 
