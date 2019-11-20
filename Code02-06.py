import turtle

## 함수 선언 부분 ##

## 함수 선언 부분 ##
myT = None

##메인 콛 부분 ##
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0, 4) :
    myT.forward(200)
    myT.right(90)

myT.done()
