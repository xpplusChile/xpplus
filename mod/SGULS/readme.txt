Antes de empezar es importante notar que la linea de comando:

g_s =  usbtmc.Instrument(0x400 , 0x09c4)

lo que hace es conectarse al generador de señales en donde 0x400 corresponde a idvendor y 0x9c4 corresponde a idproduct

Las funcione a usar son:

configGS_CH1(signal="pulse",polarity="inverted", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL")
  Esta funcion configura los parametros del generador de señales teniendo mas opciones integradas para la señal de tipo pulso, signal= define el tipo 
  de señal,polarity= es para setear si el pulso de la señal es invertido (inverted) o normal (normal) ,frec= setea la frecuencia, vhl es para setear el
  high level voltage, vll es para el low level voltaje, width= es para definir el ancho  de la señal con valor minimo ingresable de 20 para frecuencias
  mayores a 24000 (los valores ingresados quedan en ns), impedance= es para fijar la impedancia y duty= es para definir el duty de la onda (es un
  porcentaje)
  Importante tener en cuenta que si se ingresan valores para width y duty al mismo tiempo estos no son compatibles y se usara el duty.

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
