Las lineas de comando:

ip_direction = "TCPIP::10.3.84.27::INSTR"
inst = visa.ResourceManager().open_resource(ip_direction)

Lo que hacen es conectar el computador con el osciloscopio a traves de la direccion ip del osciloscopio la cual es TCPIP::10.3.84.27::INSTR
Para que esto funcione el computador y el osciloscopio tienen en estar conectados a la misma red de internet, este modulo fue usado usando cables LAN 
para conectar el osciloscopio y el computador a internet
