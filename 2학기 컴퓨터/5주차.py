# 수업(5주차)은 수업교재의 단원 Ch.5(조건문) 중심으로 학습하게 됩니다

# 라이브러리(모듈) / 명령어 및 관련 연산자 : random, if, if~else, or, str
# CH05-Lab03 주민등록번호 뒷자리 의미, 이런 뜻이?!

import random				# 난수 모듈을 불러옴 : 라이브러리
print("주민등록번호의 성별 정보 번호를 생성합니다.")

gender = random.randrange(4)
gender = gender + 1
print("생성번호: " + str(gender))	   	  # 문자와 숫자 연결하여 출력할 때를 주의
if gender == 1 or gender == 3:	                  # gender가 1 또는 3이면 남성
	print("남성입니다")
else :					          # gender가 2 또는 4이면 여성
	print("여성입니다")
print("프로그램을 종료합니다.")

#-------------------------------------------------------------------------------
year = int(input("연도를 입력하시오: "))
if ( (year % 4 ==0 and year % 100 != 0) or year % 400 == 0):
    print(year, "년은 윤년입니다.")
else :
    print(year, "년은 윤년이 아닙니다.")



a=float(input("a값 입력: "))
b=float(input("b값 입력: "))
c=float(input("c값 입력: "))

D = b*b - 4*a*c

if D > 0 :
    print("방정식의 근은 서로 다른 두 실근입니다.")
elif D == 0 :
    print("방정식은 서로 같은 두 실근(중근)입니다.")
else :
    print("방정식은 서로 다른 두 허근입니다.")

#-------------------------------------------------------------------------------
# 수업(5주차)은 수업교재의 단원 Ch.5(조건문) 중심으로 학습하게 됩니다
# 명령어 및 관련 연산자 : if~elif~else, 관계 연산자(>, <, ==)
# 라이브러리(모듈) 및 함수
# -> turtle, Turtle, shape, penup, pendown, goto, circle 


import turtle
t = turtle.Turtle( )
t.shape("turtle")
x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

t.penup( )
t.goto(x1, y1)
yy1 = y1 - r1		# circle( )의 특성으로 인해 원을 그리는 위치 조정
t.goto(x1, yy1)
t.pendown( )
t.circle(r1)

t.penup( )
t.goto(x2, y2)
yy2 = y2 - r2		# circle( )의 특성으로 인해 원을 그리는 위치 조정
t.goto(x2, yy2)
t.pendown( )
t.circle(r2)
x1=4
x2=2
y1=4
y2=2
dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5  	#두 원의 중심사이의 거리
print(16**0.5)
if dist == 0:
    turtle.write("동심원")
elif dist == r1 - r2:
    turtle.write("내접")
elif r1 - r2 < dist < r1 + r2:
    turtle.write("두 점에서 만납니다.")
elif dist > r1 + r2:
    turtle.write("만나지 않고 외부에 있습니다.")
elif dist == r1 + r2:
    turtle.write("외접")
elif dist < r1 - r2:
    turtle.write("만나지 않고 내부에 있습니다.")

