Para conectarse a la red pitaya es necesario estar conectado a la misma red, actualmente es por Lan, cuando este sea el caso se hace "sudo nmap -sP 10.3.84.1-254" y se revisa los resultados, el que nos interesa es la IP asociada a "instrumentation technologies", luego de esto se hace ssh con usuario root y con la ip obtenida, por ejemplo "ssh root@10.3.84.14" y se ingresa la contraseña.

Al ingresar "df -h" en la consola de la red pitaya se encuentra que la memoria en la cual se guardan los datos tiene un maximo de 3.7G, una vez
eliminados todos los datos tomados de la memoria usando nuvamente "df -h" la memoria ocupada es de 845M y se nos indica que la memoria disponible
es de 2.7G a pesar de que con una calculadore podemos ver que la memoria disponible es de 2.87G

Se hicieron varios scrips en bash para automatizar varios procesos de la red pitaya a traves de cron, estos son:

pitaya.py: este crip revisa la cantidad de archivos en la carpeta en la cual se guardan los datos adquiridos y si la cantidad es mayor a la estipulada 
dentro del script (4 por defecto) todos los archivos exceptuando el ultimo (al que se le esta agregando datos actualmente) son enviados al servidor de 
lago y luego borrarlos.

startup.sh : este scrip lo que haces es dejar configurado el sistema al momento que se prende (gracias a cron) e inicia automaticamente la toma de 
datos, en caso de que la adquisicion de datos se considere inestable se calcula el tiempo que falta para el minuto 1 de la hora que sigue de tal
forma que no se solape la toma de datos con la iniciada por DAQ.sh

DAQ.sh     : este scrip al minuto 1 de cada hora inicia (gracias a cron) una toma de datos con timeout de 1h para evitar el problema que se presentaba
anteriormente en el cual la hora de los datos indicada por el nombre del archivo era incorrecta

create_log.sh: este scrip guarda informacion de la red pitaya cada minuto un un archivo por nombre log_dia_mes_año.txt , la informacion contenida 
por cada minuto corresponde a si la red pitaya se encuentra conectada a internet, la configuracion de esta y los procesos que estan corriendo 
relacionados con la toma de datos

reboot.sh: este scrip hace una secuencia de bajada para el alto voltaje entregado por ambos canales y procede a reiniciar la red pitaya

turnoff.sh: este scrip hace una secuencia de bajada para el alto voltaje entregado por ambos canales y procede a apagar la red pitaya

menu.sh : permite cambiar la configuracion que se hace cada vez que se prende la red pitaya de forma interactiva y por ende hay que reiniciar la
red pitaya para que estos cambios sean efectivos
