
import serial, time
from datetime import datetime
comN = input("\n 장치관리자시리얼 번호입력: ")
#Baud = input("\n 9600 \n 19200 \n")
#print  ("com" +comN)



select = input("\n1:공단단상(미포함) \n2:공단삼상(미포함) \n3:종료 \n")
print("국번은 1번입니다")
if select == '1':
        #단상
        req = [0x7e, 0x01, 0x01, 0xD1, 0x88]
        res = [0x7E,0x01,0x02,0x00,0x1A,   #001a 총길이 26자
                0x00,0xDC,
                0x00,0x96,
                0x00,0x0A,
                0x00,0xDC,
                0x00,0x96,
                0x00,0x0A,
                0x03,0xE7,
                0x02,0x58,
                0x00,0x00,
                0x00,0x00,
                0x00,0xFF,
                0xFF,0xFF,
                0x00,0x01,  #여기까지 26자
                0x38,0xA2]  #CRC

elif select == '2': 
        #삼상
        req = [0x7e, 0x01, 0x07, 0x51, 0x8A]
        res = [0x7E,0x01,0x08,0x00,0x26,   #0026 총길이 38자
                0x00,0xDC,
                0x00,0x96,
                0x00,0x00,0x00,0x0a,
                0x00,0xdc,
                0x00,0xdc,
                0x00,0xdc,
                0x00,0x96,
                0x00,0x96,
                0x00,0x96,
                0x00,0x00,0x00,0x0a,
                0x03,0xE7,
                0x02,0x58,
                0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0xFF,
                0x00,0x01,  #여기까지 38자
                0xc4,0x9d]  #CRC
else:
    print("종료")
    exit()

def ts():
    return datetime.fromtimestamp(time.time())

def do():
    con = serial.Serial("com" + comN, 9600)

    while True:
        if con.isOpen():
            result = con.read(5)
            print(ts(), result.hex())
            con.flushInput()
            con.flushOutput()
            time.sleep(0.1)

            if len(result) == 5:
                correct = True
                for i in range(0, 5):
                    if req[i] != result[i]:
                        correct = False
                        break

                if correct:
                    con.write(res)
        else:
            con.open()

while True:
    try:
        do()
    except Exception as e:
        print("예외")
        print(e)
