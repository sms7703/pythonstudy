
    choice = input("\n 1.1


    def convert_to_bases(number):
    try:
        number = int(number)  # 입력값을 정수로 변환
        print(f"10진수: {number}")
        print(f"2진수: {bin(number)}")
        print(f"8진수: {oct(number)}")
        print(f"16진수: {hex(number)}")
        print(f"32진수: {format(number, 'b')}")
        print(f"ASCII: {ORD(number)}")
    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    user_input = input("변환할 숫자(10진수)를 입력하세요: ")
    convert_to_bases(user_input)