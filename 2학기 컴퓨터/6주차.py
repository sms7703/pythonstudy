#202212909 설민수 6주 차 과제 제출합니다
while True:
    choice = input("\n숫자선택:\n 1 (정수문제) \n 2 (배송료문제) \n")  #선택

    if choice == '1':

        n = int(input("정수를 입력하시오: "))
        if n > 0:
                print("양수")
    #Q(1-1) 
        elif n == 0:
                print("0")
    #Q(1-2)
        else:
                print("음수")

    elif choice == '2':
        country = input("국가를 입력하시오: ")
        state = input("도를 입력하시오: ")

        shipping_cose = 0
        if country == "한국":
    #Q(2-1) 
            if state == "제주도":
                shipping_cose = 10000
    #Q(2-2)       
            elif state == "부산":
                shipping_cose = 5000
        else :
                shipping_cose = 20000

        print("배송료는", shipping_cose, "입니다")
        break
    elif choice == '4':
        ct = input("국가를 입력하세요: ")
        st = input("도시입력하세요: ")
        money = 0
        if ct == '한국':
            
            if st == '부산':
                money = 5000
            elif st == '제주도':
                money = 10000
            else:
                print("다시 입력하세요")
        else:
            money= 50000
        print("금액은",money, "입니다")
        break
    
    
    
    
    
    
    else:
        print("없는 숫자입니다")
#20231016 17:09완료