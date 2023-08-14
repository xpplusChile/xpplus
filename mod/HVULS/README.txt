primero mencionar que en la linea de codigo 8 (inst=rm.open_resource("ASRL/dev/ttyACM0::INSTR")) el ASRL/dev/ttyACM0::INSTR indica la direccion del instrumento conectado por usb y dada por el computador, todos los dispositivos conectados al computador se pueden ver a traves de:

import pyvisa as visa

rm = visa.ResourceManager()
print(rm.list_resources())

Otro detalle a mencionar es que DT_READ es el tiempo de descanso despues de cada lectura y DT_WRITE es el tiempo de descanso despues de cada escritura en el intrumento, estos valores no pueden ser cero ya que des ser el dispositivo solo tomaria el ultimo comando recibido e ignoraria los anteriores.

Ahora con las funciones:

HV_W(command)  
 Se pone el comando que se quiere mandar a la maquina dentro del parentecis y esta lo ejecuta
 
HV_R(command)  
 Se pone el comando que se quiere mandar a la maquina dentro del parentesis y te devuelve el valor preguntado
 
HV_Conf(CH=0, vset=1700, iset=400 , rup=30 , rdown=50 , trip= 2  ,imonrange="high", powerdown="kill") 
 Configura un solo canal de la fuente de alto voltaje, CH indica el canal el cual se va a configurar, muy importante tener en cuenta que el primer canal 
 se  denomina 0, vset indica cual sera el voltaje onjetivo a llegar, iset es la corriente maxima que puede indicar el dispositivo antes de trippear, 
 rup indica la velocidad con la que sube el voltaje para llegar al vset, rdown indica la velocidad con que baja el voltaje para llegar al vset o llegar
 a un valor cercano a 0 una vez se decide apagar el canal en cuestion, trip indica cuanto tiempo puede estar el dispositivo por sobre la corriente 
 seteada antes de trippear


get_HV_par(CH=0, par = "NULL") 
 Se ingresa el parametro que se desea monitoriar en par="" y tambien el canal que se desea monitoriar con CH=
 Este monitoreo solo es instantaneo
                               
HV_mon(CH=0, seg=DT_READ, par = "NULL")
 Funciona igual que la funcion anterior solo que se puede ingresar seg= para determinar el tiempo por el cual se desea monitorear un parametro

HV_mon(CH=0, seg=DT_READ, par = "NULL") 
 Hace lo mismo que la funcion anterior solo que por un tiempo determinado, este tiempo se ingresa con seg=

HV_ON(CH=0) 
 Se usa para prender un unico canal indicado con CH=

HV_OFF(CH=0) 
 Se usa para apagatr un unico canal indicado con CH=

HV_ON_ALL() 
 Prende todos los canales

HV_OFF_ALL() 
 Apaga todos los canales
 
Por su repetido uso se agreagron las funciones:

HV_imon_f(CH=0): hace un loop en donde intenta obtener el valor de la corriente hasta que retorne un string que se pueda pasar a un numero. 

HV_vmon_f(CH=0): hace un loop en donde intenta obtener el valor del voltaje hasta que retorne un string que se pueda pasar a un numero. 

Los posibles parametros a monitorear son:
 

VSET    |VSET value
VSRES   |Resolution of VSET in Volt
VSDEC   |Decimal digits of VSET
VMAX    |Max value of VSET
VMIN    |Min value of VSET
VMON    |VMON value
VMRES   |VMON resolution
VMDEC   |Decimal digits of VMON
ISET    |ISET value
ISRES   |Resolution of ISET in μA
IMAXH   |Max value of ISET in high range
IMAXL   |Max value of ISET in low range
IMIN    |Min value of ISET
ISDEC   |Decimal digits of ISET
IMON    |IMON value
IMRANGE |IMON range (high /low)
IMRESL  |IMON resolution in low range
IMRESH  |IMON resolution in high range
IMDECL  |Decimal digits of IMON in low range
IMDECH  |Decimal digits of IMON in high range
MAXV    |VMAX value
MVMIN   |VMAX minimum value
MVMAX   |VMAX maximum value
MVRES   |VMAX resolution
MVDEC   |Decimal digits of VMAX
PDWN    |Power down mode Ramp / Kill
POL     |Polarit
RUP RAMP|UP value
RUPMIN  |RAMP UP minimum value
RUPMAX  |RAMP UP maximum value
RUPRES  |RAMP UP resolutionRUPDEC Decimal digits of RAMP UP
RDW RAMP|DOWN value
RDWMIN  |RAMP DOWN minimum value
RDWMAX  |RAMP DOWN maximum value
RDWRES  |RAMP DOWN resolution
RDWDEC  |Decimal digits of RAMP DOWN
TRIP    |Trip value
TRIPMIN |Trip minimum value
TRIPMAX Trip maximum value
TRIPRES Trip resolution
TRIPDEC Decimal digits of Trip
ZCDTC Status of ZC Detect; ON = offset current is getting stored; OFF = ready to store offset current
ZCADJ Status of ZC Adjust (EN/DIS)
STAT |Status
     |IS_ON     |1      |Channel On
     |IS_UP     |2      |Channel Ramping Up
     |IS_DOWN   |4      |Channel Ramping Down
     |IS_OVC    |8      |Channel in Overcurrent
     |IS_OVV    |0x10   |Channel in OverVoltage
     |IS_UNV    |0x20   |Channel in UnderVoltage
     |IS_MAXV   |0x40   |Channel in MaxV
     |IS_TRIP   |0x80   |Channel in Trip
     |IS_MAXPW  |0x100  |Channel in MaxPower
     |IS_TWARN  |0x200  |Channel in Temperature warning (>80°C)
     |IS_OVT    |0x400  |Channel in OVT (>125°C)
     |IS_KILL   |0x800  |Channel Killed
     |IS_INTLCK |0x1000 |Channel in Interlock
