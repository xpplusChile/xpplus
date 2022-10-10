primero mencionar que en la linea de codigo 8 (inst=rm.open_resource("ASRL/dev/ttyACM0::INSTR")) el ASRL/dev/ttyACM0::INSTR indica la direccion del instrumento conectado por usb y dada por el computador, todos los dispositivos conectados al computador se pueden ver a traves de:

import visa

rm = visa.ResourceManager()
print(rm.list_resources())

Otro detalle a mencionar es que DT_READ es el tiempo de descanso despues de cada lectura y DT_WRITE es el tiempo de descanso despues de cada escritura en el intrumento, estos valores no pueden ser cero ya que des ser el dispositivo solo tomaria el ultimo comando recibido e ignoraria los anteriores.

Ahora con las funciones:

HV_W(command)  se pone el comando que se quiere mandar a la maquina dentro del parentecis y esta lo ejecuta
 
HV_R(command)  se pone el comando que se quiere mandar a la maquina dentro del parentesis y te devuelve el valor preguntado
 
HV_Conf(CH=0, vset=1700, iset=400 , rup=30 , rdown=50 , trip= 2  ,imonrange="high", powerdown="kill") configura un solo canal de la fuente de alto voltaje, CH indica el canal el cual se va a configurar, muy importante tener en cuenta que el primer canal se denomina 0, vset indica cual sera el voltaje onjetivo a llegar, iset es la corriente maxima que puede indicar el dispositivo antes de trippear, rup indica la velocidad con la que sube el voltaje para llegar al vset, rdown indica la velocidad con que baja el voltaje para llegar al vset o llegar a un valor cercano a 0 una vez se decide apagar el canal en cuestion, trip indica cuanto tiempo puede estar el dispositivo por sobre la corriente antes de trippear


get_HV_par(CH=0, par = "NULL") se ingresa el parametro que se desea monitoriar en par="" y tambien el canal que se desea monitoriar con CH=
                               Este monitoreo solo es instantaneo
                               


HV_mon(CH=0, seg=DT_READ, par = "NULL") hace lo mismo que la funcion anterior solo que por un tiempo determinado, este tiempo se ingresa con seg=


HV_ON(CH=0) se usa para prender un unico canal indicado con CH=

HV_OFF(CH=0) se usa para apagatr un unico canal indicado con CH=

HV_ON_ALL() prende todos los canales

HV_OFF_ALL() apaga todos los canales
 
 
Los posibles parametros a monitorear son:
