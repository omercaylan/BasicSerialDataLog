import time
import serial

file = open("log.txt","a",encoding='utf-8')
SerialPort = serial.Serial()
SerialPort.baudrate = 115200
SerialPort.port = 'COM3'

SerialPort.open()
print("SerialPort.is_open = ",SerialPort.is_open)

while True:
    readData=SerialPort.readline()
    print(readData)
    file.write(str(readData))
    file.write("\n")

SerialPort.close()