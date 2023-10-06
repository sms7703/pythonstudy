# echo-client.py

# ...

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((119.205.235.142, 10443))
    s.sendall(connet)
    data = s.recv(1024)

print(f"Received {data!r}")




'''
pip install pyserial 설치
또는
connetda install pyserial
'''


import serial
import time

from datetime import datetime

request = [0x7e, 0x02, 0x01, 0xD1, 0x78]
response = [0x7E,0x02,0x02,0x00,0x1A,0x00,0xDC,0x00,0x96,0x00,0x0A,0x00,0xDC,0x00,0x96,0x00,0x0A,0x03,0xE7,0x02,0x58,0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0xFF,0x00,0x01]

def handler():
    return datetime.fromtimestamp(time.time())


def parsing():
    #port : com
    #baud : 9600
    connet = #

    while True:
        if(connet.isOpen()):
            result = connet.read(5)
            print(handler(), result.hex())
            connet.flushInput()
            connet.flushOutput()
            time.sleep(0.1)
            
            if(len(result)==5):
                correct = True
                for i in range(0, 5):
                    if(request[i]!=result[i]):
                        correct=False
                        break

                if(correct):
                    connet.write(response)
                    
        else:
            connet.open()


while True:
    try :
        parsing()
    except Exception as e:
        print("예외")
        print(e)
    
