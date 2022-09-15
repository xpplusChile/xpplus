Las lineas de comando:

ip_direction = "TCPIP::10.3.84.27::INSTR"
inst = visa.ResourceManager().open_resource(ip_direction)

Lo que hacen es conectar el computador con el osciloscopio a traves de la direccion ip del osciloscopio la cual es TCPIP::10.3.84.27::INSTR
Para que esto funcione el computador y el osciloscopio tienen en estar conectados a la misma red de internet, este modulo fue usado usando cables LAN 
para conectar el osciloscopio y el computador a internet

Este modulo cuenta con la funcion:

get_data()
  La cual por defecto guarda la informacion del canal 1 del osciloscopio, hace un solo trigger y guarda hasta 100000 puntos, importante notar que si
  la cantidad de puntos en pantalla es menor a la utilizada por defecto solamente se guardaran la cantidad en pantalla, si la cantidad de puntos en 
  pantalla es mayor solamente se guardaran 100000 puntos
  Si por ejemplo se quiere guardar la informacion de tres canales hay que escribir get_data(channel="1,2,3") siendo muy importante notar que se guardara 
  solamente la informacion del canal 1,2 y 3 y no esta la posibilidad de guardar la informacion en los canales 1,2 y 4
  

