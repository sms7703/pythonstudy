P = "도서관에서 보자"
"            -3-2-1   -3은 띄어쓰기    "
"    01234567               "


S = "Hello1Python2Language"
a = "test"

print("평문 :", P)
print("암호문 :", P[-1 : -9 : -1])
" P = 도서관에서 보자"
"첫번째 -1    :시작 : 자"
"두번째 -9(+1):종료 : 자보 서에관서도"
"세번째 -1    :우 -> 좌 간격1"


print("암호문 :", P[-2 : -7 : -2])
print("암호문 :", P[-1 : -7 : -1])
print("테스트관련 :", a[2 : 1 : -1])

print(S[7 : 13 : 1])
print(S[-7 : -2 : 1])
print(S[-7 : 2 : -1])
print(S[-7 : 2 : -2])
print("S암호문5:",S[0 : 13 : 2])
" S = Hello1Python2Language" 
"첫번째  0    :시작 : H"
"두번째 13    :종료 : Hello1Python2"
"세번째 2     :간격 : HloPto2"

print("S암호문6:",S[-1 : -8 : -1])