import serial 
import time
import os

#criar conexão 
porta = "COM6"
arduino = serial.Serial(porta, 9600, timeout = 1)
time.sleep(1)

while True:
    comando = input("Digite 0 para desligar o LED1 ou 3 para desligar o LED2, 1 para ligaro LED1 ou 3 para ligar o LED2 ou 2 para encerrar o programa: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if comando == '1':
        arduino.write(b'1')
        print("LED Ligado!")

    elif comando == '0':
        arduino.write(b'0')
        print("LED Desligado!")

    if comando == '4':
        arduino.write(b'4')
        print("LED2 Ligado!")

    elif comando == '3':
        arduino.write(b'3')
        print("LED2 Desligado!")

    elif comando == '2':
        arduino.write(b'0')
        arduino.write(b'3')
        print("Programa encerrado!")
        break

    else:
        print("comando Invalido!")
        print("O comando precisar ser 0, 1 ou 2")

arduino.close()
