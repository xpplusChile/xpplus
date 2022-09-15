Antes de empezar es importante notar que la linea de comando:

g_s =  usbtmc.Instrument(0x400 , 0x09c4)

lo que hace es conectarse al generador de señales en donde 0x400 corresponde a idvendor y 0x9c4 corresponde a idproduct

Las funcione a usar son:
configGS()
  Esta funcion por defecto configura el generador de señales con signal="pulse", frecuencia=24000 ,high level voltaje = 0.5 , low level voltaje= -0.5 
  ,width= 20 ,impedance=50, para configuarlo de otra forma se puede hacer por ejemplo signal="pulse", frec=50000 ,vhl=0 ,vll= -0.8 ,impedance=100, duty=80 
  El witdh esta en unidad de medida ns,el duty es un porcentaje y los voltajes estan en vpp

GS_ON()
  Prende el canal 1 del generador de señales

GS_OFF()
  Apaga el canal 1 del generador de señales
 
GS(command)
  Manda un comando al generador de señales dando usando time.sleep para evitar problemas
