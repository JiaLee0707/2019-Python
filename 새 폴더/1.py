Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello, world!")
Hello, world!
>>> 10 + 20
30
>>> 9876 * 27 - 32767
233885
>>> a=100
>>> b=50
>>> result=a+b
>>> print(result)
150
>>> 
====================== RESTART: C:\Python\Code02-01.py ======================
100 + 50 = 150
100 - 50 = 50
100 * 50 = 5000
100 / 50 = 2.0
>>> 
====================== RESTART: C:\Python\Code02-02.py ======================
100
50
100 + 50 = 10050
Traceback (most recent call last):
  File "C:\Python\Code02-02.py", line 5, in <module>
    result = a - b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
====================== RESTART: C:\Python\Code02-03.py ======================
100
50
100 + 50 = 150
100 - 50 = 50
100 * 50 = 5000
100 / 50 = 2.0
>>> 
====================== RESTART: C:\Python\Code02-04.py ======================
첫 번째 숫자를 입력하세요 : 100
두 번째 숫자를 입력하세요 : 50
100 + 50 = 150
100 - 50 = 50
100 * 50 = 5000
100 / 50 = 2.0
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape("turtle")
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(100)
>>> t.shape("turlte")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.shape("turlte")
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named turlte
>>> 
