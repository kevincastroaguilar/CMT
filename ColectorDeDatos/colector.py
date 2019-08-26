
# Este codigo en python es capaz de leer los datos seriales que genera el arduino.
# Debemos importar la libreria serial, para instalarla deben abrir el cmd y escribir: python -m pip install pyserial
# Iniciamos una variable llamada lecturaArduino, que almacenara el String obtenido del puerto serial
# serial.serial tiene 3 parametros (el primero "COM7" es el puerto al que esta conectado el arduino, deben revisarlo con el que aparece en Arduino IDE)

import serial
lecturaArduino = ""
lecturaArduino = serial.Serial('COM7', baudrate=9600, timeout=1.0)

# Iniciamos un while loop que estara activo mientras sea "verdadero"(el puerto este conectado) 
# Y este while imprimira en consola con un "print", cada segundo que obtiene el valor
while True:
    line = lecturaArduino.readline()
    print(line)
