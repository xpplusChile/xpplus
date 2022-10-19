primero mencionar que en la linea de codigo 8 (usb_direction = "USB0::6833::3601::DP8C234806315::0::INSTR") el "USB0::6833::3601::DP8C234806315::0::INSTR" 
indica la direccion del instrumento conectado por usb y dada por el computador, todos los dispositivos conectados al computador se pueden ver a traves de:

import pyvisa as visa

rm = visa.ResourceManager()
print(rm.list_resources())

Otro detalle a mencionar antes de ver las funciones es que DT_READ y DT_WRITE son los tiempos de descanso(downtime) entre comandos de lectura y escritura respectivamente.

LV_W(command)
  Manda un comando de escritura al dispositivo con tiempo de descanso.
 
LV_R(command)
  Manda un comando de lectura y devuelve la respuesta del dispositivo.

LV_Conf(CH=1, volt=0, curr=0, curr_prot="NULL", volt_prot="NULL"):
  Hace una configuracion siCH= define el canal a configurar
