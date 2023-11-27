a = [123, 45, 67, 89 ,10]
b = [123, 10, 10, 23 ,10]


r_list = set(a) & set(b)

if list:
    print("공통값은", list(r_list))
else:
    print("없습니다")