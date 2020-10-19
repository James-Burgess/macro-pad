from time import sleep
import serial



ser = False
while not ser:
    try:
        ser = serial.Serial('/dev/ttyUSB1', 9600)
    except serial.SerialException:
        sleep(.5)

while True:
     input = ser.readline().decode("utf-8").strip()

     print(input)
     if input == "trigger: camel":
         print('doing some cool shit')

     sleep(.1) # Delay for one tenth of a second
