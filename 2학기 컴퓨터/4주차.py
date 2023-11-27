while True:
  
  choice = input("\n 1.암호문 \n 2.소금물 \n 3.그외 \n")

  if choice == '1':
      P = "도서관에서 보자"
      "            -3-2-1   -3은 띄어쓰기    "
      "    01234567               "
      S = "Hello1Python2Language"
      a = "test"
      print("테스트중 :", P[-7 : -4 : -1])
      print("평문 :", P)
      print("암호문 :", P[-1 : -3 : -1])
      " P = 도서관에서 보자"
      "첫번째 -1    :시작 : 자"
      "두번째 -9(-1):종료 : 자보 서에관서도"
      "세번째 -1    :우 -> 좌 간격1"
#답은-7:도  2-1 : 도 

#-7:3  (2-1):1
      print("보서관 :", P[-2 : -7 : -2])
      #ㅊ> (-2):보 (-8):도  -> -2: 보서관
      
      print("암호문1-2 :", P[-1 : -7 : -1])
      #자보 서에관서도 -> 자보 서에관-(8)  -> -1:자보 서에관
      
      print("TEST :", a[3 : 1 : -1])
      #(3):S    (1)ST
      #TEST ->S
      
      #  S = "Hello1Python2Language"
      print(S[7 : 13 : 1])
      #y(7)thon2(12)  =ython2
      
      print(S[-7 : -2 : 1])
      #a(-7)nguage(-3)  =angua
      
      print(S[-7 : 2 : -1])
      #a(-7)Hello1Python2La(1) ->반대로(-1) ->aL2nohtyP1olleH
      
      print(S[-7 : 2 : -2])
    #a(-7)Hello1Python2La->반대로2 ->(a)L(2)n(o)h(t)y(P)1(o)l(l)e(H) = a2otPo1H
      print("S암호문5:",S[0 : 13 : 2])
      " S = Hello1Python2Language" 
      "첫번째  0    :시작 : H"
      "두번째 13    :종료 : Hello1Python2"
      "세번째 2     :간격 : HloPto2"

      print("S암호문6:",S[-1 : -8 : -1])
      continue
      
  if choice == '2':
    print("소금물의 농도 문제 입니다")
  
    salt = int(input("소금 몇 gm: "))
    water = int(input("물의 몇ml: "))
    test = salt / (salt+water) *100
    print("소금물의 농도는 " + str(test) + "%")
    break
