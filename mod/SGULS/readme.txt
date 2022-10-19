Antes de empezar es importante notar que la linea de comando:

g_s =  usbtmc.Instrument(0x400 , 0x09c4)

lo que hace es conectarse al generador de señales en donde 0x400 corresponde a idvendor y 0x9c4 corresponde a idproduct

Las funcione a usar son:
configGS_CH1(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL")
  Esta funcion por defecto configura el generador de señales con signal="pulse", frecuencia=24000 ,high level voltaje = 0.5 , low level voltaje= -0.5 
  ,width= 20 ,impedance=50, para configuarlo de otra forma se puede hacer por ejemplo signal="pulse", frec=50000 ,vhl=0 ,vll= -0.8 ,impedance=100, duty=80 
  El witdh esta en unidad de medida ns,el duty es un porcentaje,los voltajes estan en vpp y solo configura el canal 1.

configGS_CH2(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL")
  Hace lo mismo que la funcion anterior pero para el canal 2.
  
configGS_ALL(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL")
  Hace lo mismo que las dos funciones anteriores pero para los dos canales a la vez.
  
GS_ON_CH1()
  Prende el canal 1 del generador de señales

GS_OFF_CH1()
  Apaga el canal 1 del generador de señales
 
GS_ON_CH2()
  Prende el canal 1 del generador de señales

GS_OFF_CH2()
  Apaga el canal 1 del generador de señales
  
GS_ON_ALL()
  Prende el canal 1 del generador de señales

GS_OFF_ALL()
  Apaga el canal 1 del generador de señales
 
GS(command)
  Manda un comando al generador de señales dando usando time.sleep para evitar problemas
