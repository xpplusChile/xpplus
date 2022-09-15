Las funcione a usar son:
configGS()
  Esta funcion por defecto configura el generador de señales con signal="pulse", frecuencia=24000 ,high level voltaje = 0.5 , low level voltaje= -0.5 
  ,width= 20 ,impedance=50, para configuarlo de otra forma se puede hacer por ejemplo signal="pulse", frec=50000 ,vhl=0 ,vll= -0.8 ,impedance=100, duty=80 
  El witdh esta en unidad de medida ns,el duty es un porcentaje y los voltajes estan en vpp

def GS_ON():
  Prende el canal 1 del generador de señales

def GS_OFF():
  Apaga el canal 1 del generador de señales
  
