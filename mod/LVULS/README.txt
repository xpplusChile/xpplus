primero mencionar que en la linea de codigo 8 (usb_direction = "USB0::6833::3601::DP8C234806315::0::INSTR") el "USB0::6833::3601::DP8C234806315::0::INSTR" 
indica la direccion del instrumento conectado por usb y dada por el computador, todos los dispositivos conectados al computador se pueden ver a traves de:

import pyvisa as visa

rm = visa.ResourceManager()
print(rm.list_resources())
